#!/usr/bin/env python

'''
tag_generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os

post_dir = '../_posts/'
draft_dir = '../_drafts/'
category_dir = '../category/'

filenames = glob.glob(post_dir + '*markdown')
filenames = filenames + glob.glob(draft_dir + '*markdown')

categories = []
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    for line in f:
        if crawl:
            current_categories = line.strip().split(':') 
            if current_categories[0] == 'categories':
                print("reading categories")
                if (current_categories[1].strip().startswith('[')):
                    clean_tag = ''.join(c for c in current_categories[1] if c not in '[]')
                    list_tags = map(str.strip, clean_tag.split(','))
                    categories.extend(list_tags)
                else: 
                    list_tags = map(str.strip, current_categories[1].strip().split())
                    categories.extend(list_tags)
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
categories = set(categories)

old_categories = glob.glob(category_dir + '*.md')
for category in old_categories:
    os.remove(category)
    
if not os.path.exists(category_dir):
    os.makedirs(category_dir)

for category in categories:
    category_filename = category_dir + category.replace(' ', '_') + '.md'
    f = open(category_filename, 'a')
    write_str = '---\nlayout: categorypage\ntitle: \"Category: ' + category + '\"\category: ' + category + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Categories generated, count", categories.__len__())
