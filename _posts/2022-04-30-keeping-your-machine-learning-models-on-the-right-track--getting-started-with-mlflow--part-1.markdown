---
layout:	post
title:	"Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 1"
date:	2022-04-30
canonical_url: https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-1-f8ca857b5971
---





---

![](/img/0*p8GDozqUW7x7xBk_)Photo by [Liu Lulu](https://unsplash.com/@doublelu?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*This post is part of series of posts on MLflow. Make sure to checkout Part 2:*

[**Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 2**  
*Learn how to use MLflow Model Registry to track, register and deploy Machine Learning Models effectively.*mlopshowto.com](https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc "https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc")
> You cannot understand what is happening today without understanding what came before [(Steve Jobs)](https://shc.stanford.edu/sites/default/files/History_broch_web_11_13.pdf)

### Machine Learning as an Empirical Science — and the importance of experiment tracking

![](/img/1*c9Md7eTk9ZYppsrpav7AJA.jpeg)E[mpirical research](https://en.wikipedia.org/wiki/Empirical_research) is **an evidence-based approach to the study and interpretation of information**. The empirical approach relies on real-world data, metrics and results rather than theories and concepts. **Empiricism** is the idea that knowledge is primarily received through experience and attained through the five senses.

[**Machine Learning** has both theoretical and empirical aspects](https://link.springer.com/content/pdf/10.1007/BF00115008.pdf). While **theory** and **concepts** are extremely important, they are not enough to achieve our objectives and validate our hypothesis —[since most learning algorithms are too complex for formal analysis.](https://link.springer.com/content/pdf/10.1007/BF00115008.pdf) **Experimentation** is also a critical part of machine learning.

In order to validate our initial hypothesis, we work with the assumption that our experiments are sufficiently **robust** and **successful**. As a byproduct, we would end up with a model which is able to **predict** outcomes for previously unseen events, based on the data which was used for **training**.

Of course, reality is much more **nuanced**, **complex** — and **less linear**— than that. More often than not we will need to test many different hypothesis, until we find one that while not bad, is mediocre at best. Many iterations later, we might end up with a satisfactory model.

### **The case for Machine Learning Model Tracking**

Being able to look back into different machine learning experiments, their **inputs**, **parameters** and **outcomes** is critical in order to iteratively improve our models and increase our chances of success.

One reason for this is that the cutting edge model that you spent days training last week might be no longer good enough today. In order to detect and conclude that, information about the inputs, metrics and the code related to that model must be available somewhere.

This is where many people might say — I’m already tracking this. And my hundred **Jupyter Notebooks** can prove that. Others might say something similar, while replacing Jupyter Notebooks with **Excel Spreadsheets**.

![](/img/1*3tRt38Rpd4Q18kgnpYNmew.jpeg)How a folder full of different Jupyter Notebooks looks likeWhile none of these approaches is inherently wrong, the process gets **challenging** and **error-prone** once you start to move along three scales:

* Number of **use cases** and **models**;
* **Scale** of your team;
* **Variety** of your models (and **data**)

In other words, you do not want to rely on **Jupyter Notebooks** and **Excel spreadsheets** when you are running **production grade machine learning systems** — you need something **structured and flexible,** which enables seamless **collaboration amongst different people and personas.**

### Introducing MLflow

![](/img/1*PQH2xK5Lt0loGkNiugFfog.png)**MLflow** is an open source project that was created by [Databricks](https://databricks.com/) — the same company behind [Apache Spark](https://spark.apache.org/) and [Delta](https://delta.io/), amazing open source projects as well.

The main objective of MLflow is to provide a unified platform for enabling collaboration across different teams involved in creating and deploying machine learning systems, such as data scientists, data engineers and machine learning engineers.

![](/img/1*DEXv7XZYCoNg91QqJWpWsw.png)A typical Machine Learning workflow using MLflowIn terms of functionalities, **MLflow** allows tracking Machine Learning experiments in a seamless way, while also providing a single source of truth for model artifacts. It has native support for a wide variety of **model flavors**— think plain vanilla **Sci-Kit Learn**, but also models trained with **R, SparkML, Tensorflow, Pytorch,** amongst others.

### Getting Started

Now that we know about experiment tracking, MLflow and why these are important in a Machine Learning project, let’s get started and see how it works in practice. We will:

* Create a free Databricks Workspace using Databricks Community Edition
* Create multiple runs for a machine learning experiment
* Compare these experiment runs
* Look at the artifacts that were generated by these runs
1. **Databricks Community Edition**

The first step is signing up to [Databricks Community Edition](https://databricks.com/product/faq/community-edition), a free version of the Databricks cloud based big data platform. It also comes with a rich portfolio of award-winning training resources that will be expanded over time, making it ideal for developers, data scientists, data engineers and other IT professionals to learn Apache Spark. On top of that, a managed installation of **MLflow** is also included.

Simply click on [this link](https://community.cloud.databricks.com/) to get started. Once you register and login, you will be presented with your Databricks Workspace.

![](/img/1*fpsNMgXEsQMaSrFxKC8lgA.png)**2. Creating a compute cluster**

In your workspace, you are able to create a small scale cluster for testing purposes. To do so, on the left hand side menu, click on the **Compute** button, and then on the **Create Cluster** button.

It is recommended to choose a runtime that supports ML applications natively — such runtime names end with **LTS ML**. By doing so, MLflow and other common machine learning frameworks will automatically be installed for you. Choose a name for your cluster and click **create**.

![](/img/1*xJN9qf0Rv25Wm-V5G1BPWQ.png)**3. Importing our Experiment Notebook**

Next, you will want to create a Databricks Notebook for training your model and tracking your experiments. To make things easier, [you can import an existing quickstart notebook](https://docs.databricks.com/notebooks/notebooks-manage.html#import-a-notebook) — but of course, if you prefer to write your own code to train your model, feel free to do so. The MLflow Quickstart Notebook used for this exercise can be found [here](https://docs.databricks.com/_static/notebooks/mlflow/mlflow-quick-start-training.html).

In a nutshell, our quickstart notebook contains code to train a Machine Learning model to predict diabetes using a sample dataset from Sci-Kit Learn. The notebook is really well documented and contains all the details about the model and the different training steps.

![](/img/1*D9XLhkMLclBr_mBn4b2yvg.png)How to import an existing Databricks Notebook**4. Running Your Notebook and Training Your Model**

The next step is running your notebook and training your model. To do so, first attach the notebook to the cluster you have previously created, and click the **Run All** button.

If you are using our quickstart notebook, you will notice that each time you train your model with different parameters, a new experiment run will be logged on MLflow.

To have a quick glance on how each experiment run looks like, you can click on the experiments button at the top right of your notebook.

A more detailed view on your experiments is available on the Machine Learning UI.

![](/img/1*KF--mmbBSe8Glp2oI0MoJw.gif)How to access the Databricks Machine Learning UIOnce you are on the Machine Learning UI, you can click on the Experiments button on the bottom of the left hand side menu. Doing so will display a detailed view of your different model runs.

![](/img/1*fnUdA2sRApbfvb5wxf9v6g.png)**5. Comparing and Analysing Experiment Runs**

You can **visually** compare **hyperparameters** and **metrics** of different experiment runs. To do so, select the models you want to compare by clicking on their checkboxes on the left hand side of the main table, and click **Compare**.

By doing so, you will be able to inspect different **hyperparameters** that were used across experiment runs, and how they affect your model metrics. This is quite useful to understand how these parameters influence your model performance and conclude which set of parameters might be best — for deploying the final version of your model into production, or for continuing further experiments.

![](/img/1*w69D0LlIplfmQjp7eUJNZQ.png)The great thing is that these results are available for you, but in a team setting, you could also share these with a wider team of **Data Scientists, Data Engineers and Machine Learning Engineers.**

**6. Model Artifacts**

In our quickstart notebook, we have code for logging model parameters (*mlflow.log\_param*), metrics (*mlflow.log\_metric*) and models (*mlflow.sklearn.log\_model*).

When you select a particular model from the table containing all experiment runs, you can see additional information related to that model, and also the artifacts related to that model.

This is also quite useful for when you want to **deploy this model into production**, since amongst the artifacts, you will have not only the *serialized* version of your model, but also a *requirements.txt* file containing a full list of **Python** environment dependencies for it.

![](/img/1*S7MdJt9_YRDCOH2TToX1TQ.png)### Main Takeaways

By this point you should have understood:

* Why **Machine Learning Experiment Tracking** is critical for success when running production grade ML
* How **MLflow** makes it seamless to track Machine Learning experiments and **centralize** different model **artifacts,** enabling easy collaboration in ML teams
* How easy it is to train your models with **Databricks** and keep them on the right track with **MLflow**

There are some more important aspects to be covered, specially when we talk about **model productionization** and **MLOps**. But these will be the topic of a next post.

### Further Reference

* [Databricks Managed MLflow](https://databricks.com/product/managed-mlflow)
* [MLflow Quickstart](https://docs.databricks.com/_static/notebooks/mlflow/mlflow-quick-start-training.html)
* [MLflow Homepage](https://mlflow.org/)
* [MLflow Documentation](https://www.mlflow.org/docs/latest/index.html)
* [What is MLOps?](https://databricks.com/glossary/mlops)
* [Machine Learning as an Experimental Science](https://link.springer.com/content/pdf/10.1007/BF00115008.pdf)

### You Might Also Like

[**Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 2**  
*Learn how to use MLflow Model Registry to track, register and deploy Machine Learning Models effectively.*mlopshowto.com](https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc "https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc")[**What is Model Drift, and How it Can Negatively Affect Your Machine Learning Investment**  
*In the domains of software engineering and mission critical systems, we cannot say that monitoring and instrumentation…*mlopshowto.com](https://mlopshowto.com/what-is-model-drift-and-how-it-can-negatively-affect-your-machine-learning-investment-ce7f5b9b6a37 "https://mlopshowto.com/what-is-model-drift-and-how-it-can-negatively-affect-your-machine-learning-investment-ce7f5b9b6a37")[**What are Feature Stores and Why Are They Critical For Scaling Machine Learning**  
*Understand why Feature Stores are critical for a good MLOps foundation*mlopshowto.com](https://mlopshowto.com/what-are-feature-stores-and-why-are-they-critical-for-scaling-machine-learning-94e14afec81d "https://mlopshowto.com/what-are-feature-stores-and-why-are-they-critical-for-scaling-machine-learning-94e14afec81d")

