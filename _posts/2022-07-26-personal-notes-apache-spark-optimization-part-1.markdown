---
layout:	post
title:	"Notes on Apache Spark Performance Optimization & Tuning, Part 1"
date:	2022-07-26
categories: [data-engineering, software-engineering]
tags: [apache-spark, performance-optimization, cost-based-optimization, adaptive-query-execution]
---





---

![](/img/marc-olivier-jodoin-NqOInJ-ttqM-unsplash.jpg)[Credit: <a href="https://unsplash.com/@marcojodoin?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Marc-Olivier Jodoin</a> on <a href="https://unsplash.com/s/photos/traffic-night?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  ](https://unsplash.com/photos/YLSwjSy7stw)

  <hr/>

  ### Some Background on Adaptive Query Execution

  * Primitive version on Spark 1.6
  * New version prototyped and experiment by Intel Big Data
  * Databricks and Intel co-engineered new AQE in Spark 3.0

  ##Performance Optimization on Spark: Cost-Based Optimization

  * Prior to **Apache Spark 3.0**, most of the possibilities around Spark Optimization were centered around  **Cost-Based Optimization**. 

  * **Cost-Based Optimization** aims to choose the best plan, but it does not work well when:
    * Stale or missing statistics lead to innacurate estimates
      * Collecting statistics and making sure cardinality estimates are accurate is costly, so this is something users struggled with. It could also be that your data hasn't changed; in this case you would be doing unecessary recalculations.
    * Statistics collection are too costly (e.g. column histograms)
    * Predicates contain UDFs
    * Hints do not work for rapidly evolving data

    

    **Adaptive Query Execution**, on the other hand, bases all optimization decisions on **accurate runtime** statistics.

    ##Query Stages

    * Shuffle or broadcast exchanges divide a query into query stages
    * Intermediate results are materialized at the end of a query stage
    * Query stage boundaries optimal for runtime optimization:
      * The inherent break point of operator pipelines
      * Statistics available, e.g. data size, partition sizes

  (*to be continued...*)





