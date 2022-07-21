---
layout:	post
title:	"About MLOps And Why Most Machine Learning Projects Fail — Part 1"
date:	2021-03-03
canonical_url: https://mlopshowto.com/about-mlops-and-why-most-machine-learning-projects-fail-part-1-6a4d76e84e86
---





---

![](/img/1*bFOIJY9nD0Vc3YQOTLq8sA.jpeg)If you have been involved with **Machine Learning** (or you are aiming to be), you might be aware that *reaping the benefits* of Machine Learning systems in real life is not a trivial task.

Well, if that is indeed the case, there are some good news — you and your company would certainly not be alone. According to [Gartner](https://blogs.gartner.com/andrew_white/2019/01/03/our-top-data-and-analytics-predicts-for-2019/), “*Through 2020, 80% of AI projects will remain alchemy, run by wizards whose talents will not scale in the organization”.* [A similar estimation by VentureBeat](https://venturebeat.com/2019/07/19/why-do-87-of-data-science-projects-never-make-it-into-production/) claims that a whopping *87% of AI projects will never make it into production.* With more and more money being poured over Machine Learning projects, that is certainly an alarming metric.

Let’s quantify this a bit. In 2019 alone, approximately **USD 40 billions** were invested into privately held AI companies. If we extrapolate this and throw the approximated success rate of AI projects into these figures (and completely exclude intracompany ML investments), we reach the conclusion that in 2019, around **USD 38 billions were wasted due to unsuccessful Machine Learning projects.**

![](/img/1*togeaW8pU_lL-Xv_pNDrKA.png)Figure 1: Total disclosed value of equity investments in privately held AI companies, by target region. Source: [Brookings Tech Stream](https://www.brookings.edu/techstream/what-investment-trends-reveal-about-the-global-ai-landscape/)Apart from the — *quite significant* — **economic** problem, that brings additional issues. Pressure mounts into existing and new ML projects and initiatives, and skepticism within the industry tends to grow. This results in a **vicious circle —***skepticism* leads to less *investments*, which leads to *less potential for scale*; consequently, *tangible benefits* associated with Machine Learning projects start to *wane*.It becomes harder and harder to justify investment in these initiatives.

But why is it so difficult? After all — *data science, machine learning, statistics*— we are talking about **exact sciences**, aren’t we? Shouldn’t this type of projects and investments be more *predictable* (no pun intended)?

### The Sexiest Job of the 21st Century

One of the issues is that **Machine Learning** is currently seen as a **gold rush**. There are many reasons for this phenomena — hype is certainly one of them. You might remember the infamous article from Harvard Business Review, who in 2021 positioned the **data scientist** as *“the sexiest job of the 21st century”.*

What was seen after that was the following:

* There was (and still is) an *avalanche of people* wanting to jump into data science (without having the skills)
* There was (and still is) and *avalanche of companies* wanting to jump into data science (without having the experience)
* The amount of data generated worldwide has grown to [*colossal proportions*](https://www.statista.com/statistics/871513/worldwide-data-created/) — but not a lot of this data has **immediate** business value, even when *cutting edge* machine learning techniques come into play. This is where adequate **data governance** and **data engineering** planning are key.
* There were (and still are) many activities inherent to **productionizing** machine learning models which are still being overlooked — both by **companies** and **wannabe data scientists & machine learning practitioners**

Here, a parenthesis is needed: there are many companies and public cloud providers excelling in the data governance and engineering space — perhaps due to the fact that these disciplines are also key for success in good old business intelligence. However, the same cannot be said about the latter item.

People are desperate to get into data science, companies are desperate to get into data science, but the bulk of what is being produced are *Machine Learning models which never make it into Production and end up in the twilight zone of Jupyter Notebooks*.

![](/img/1*t7Mrhy8PtZn7YafxxynRfA.jpeg)What was once a cutting edge ML model. Source: [Ante Hamersmit / Unsplash](https://unsplash.com/@ante_kante)### Looking for Answers

While HBR’s infamous article was published in 2012; it took around two years for another landmark article to see the light of day. In “[Machine Learning: The High Interest Credit Card of Technical Debt](https://research.google/pubs/pub43146/) (2014)”, researchers from Google claimed:


> (…) we note that it is remarkably easy to incur massive **ongoing maintenance costs** at the system level when applying **machine learning**. The goal of this paper is highlight several machine learning specific **risk factors** and **design patterns** to be **avoided** or **refactored** where possible. These include **boundary erosion**, **entanglement**, **hidden feedback loops, undeclared consumers, data dependencies, changes in the external world, and a variety of system-level anti-patterns.**

It was the first time someone raised the importance of thinking about *machine learning productionization* as a discipline in itself — at least in the tech **mainstream.**

[**What is Kubernetes and Why it is so Important for Machine Learning Engineering and MLOps**  
*If you follow up technology trends, data science, artificial intelligence and machine learning, chances are that you…*mlopshowto.com](https://mlopshowto.com/what-is-kubernetes-and-why-it-is-so-important-for-machine-learning-engineering-and-mlops-96249a7a279e "https://mlopshowto.com/what-is-kubernetes-and-why-it-is-so-important-for-machine-learning-engineering-and-mlops-96249a7a279e")### A Blast from the Past

Looking at the most critical aspects mentioned by Google Researchers, one might see an overlap with another science that has been around for quite a while. A discipline that has allowed for immense innovation in the form of things that are part of our daily lives, from **airspace controlling** to **social networks**, **electronic bank transactions** and whatnot. Yes, I am talking about **Software Engineering**.

![](/img/1*ZP1ou9XmW5SWQn7cFQJ9xA.jpeg)[Source: Unsplash](https://unsplash.com/@wocintechchat)**Machine Learning** has already been part of any CS curriculum for at least 50 years. That brings us a follow up question — **why** has it taken so long for us in the ML industry to connect the dots and leverage software engineering best practices?

The answer might be in the fact that besides being around for many years, **software engineering** practices have changed **dramatically** in recent years, specially with the advent of **Agile** and **DevOps**. Which are proving to be key concepts in **productionizing** **machine learning** systems and thus increasing its **business potential**.

### The Case for MLOps

![](/img/1*F5ttVjpTwFamneQ0yHtqlA.png)MLOps cycle. Source: ml-ops.orgCompanies such as Deep Learning startup [Paperspace](https://techcrunch.com/tag/paperspace/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAF2zDZY_5qHqGm6Am_HzNRAMOSnF8M6YUxxcKvLcc7HrJkr7UvSaMs7B8vrMI4hjO8afmWnihOI9itFaO75sy_fTy54L6x3FqISX3dGaG8CbygPB4MbeEiFLYpaXg-Yn1Gw4LVVOblGdtLzSrfokGczHOPZFkdjabO10mrI5qtwx) have been pointing at the issues in this topic in a more *concrete* fashion:


> Here are a few examples: an absurd amount of work happens on **siloed desktop computers (even to this day)**; there’s practically **zero automation** (e.g. automated tests); collaboration is a mess; **pipelines are hacked together with a constellation of home-rolled and brittle scripts**; **visibility** is practically non-existent when it comes to models deployed to **development, staging, and production**; **CI/CD is a foreign concept**; **model versioning** is difficult for many organizations to even define; **rigorous health and performance monitoring of models is extremely rare**, and the list goes on.

This is where **Machine Learning Operations (MLOps)** comes to the rescue. **MLOps** borrows concepts from **DevOps**, such as **Continuous Delivery (CD)**, while adding new concepts, such as **Continuous** **Training (CT), Monitoring** and **Observability.**

[**A Journey Into Machine Learning Observability with Prometheus and Grafana, Part I**  
*Deploying Prometheus and Grafana on Kubernetes in 10 minutes for basic infrastructure monitoring*mlopshowto.com](https://mlopshowto.com/a-journey-into-machine-learning-observability-with-prometheus-and-grafana-part-i-384da4b2d77f "https://mlopshowto.com/a-journey-into-machine-learning-observability-with-prometheus-and-grafana-part-i-384da4b2d77f")There are other disciplines which while not exactly related to MLOps, play equal importance, such as **fairness**, **explainability**, **scalability**, **performance**, **security** and **integrity**. Besides not being directly related to machine learning systems output, it becomes clear that these concepts become more and more important as machine learning systems and applications evolve.

This is where we come to the purpose of this website. We will cover not only the **what** and the **why** of **MLOps**, but most importantly the **how** — not only from a **conceptual** perspective, which is important, but also from the **practical** side.



