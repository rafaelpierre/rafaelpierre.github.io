---
layout:	post
title:	"Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 2"
date:	2022-07-20
canonical_url: https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc
---





---

![](/img/1*YaW_cGaqs53d2SAosre-Rg.jpeg)[Credit: Alfons Morales (Unsplash)](https://unsplash.com/photos/YLSwjSy7stw)**TLDR**; ***MLflow Model Registry*** *allows you to keep track of different Machine Learning models and their versions, as well as tracking their changes, stages and artifacts.* [*Companion Github Repo*](https://github.com/rafaelvp-db/mlflow-getting-started) *for this post*

In our last post, we discussed the importance of **tracking Machine Learning experiments, metrics and parameters**. We also showed how easy it is to get started in these topics by leveraging the power of [MLflow](https://www.mlflow.org/) (for those who are not aware, **MLflow** is currently the de-facto standard platform for machine learning experiment and model management).

[**Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 1**  
*Learn why Model Tracking and MLflow are critical for a successful machine learning project*mlopshowto.com](https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-1-f8ca857b5971 "https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-1-f8ca857b5971")In particular, **Databricks** makes it even easier to leverage **MLflow**, since it provides you with a completely managed version of the platform.

This means you don’t need to worry about the underlying infrastructure to run MLflow, and it is completely integrated with other Machine Learning features from Databricks Workspaces, such as [Feature Store](https://databricks.com/blog/2021/05/27/databricks-announces-the-first-feature-store-integrated-with-delta-lake-and-mlflow.html), [AutoML](https://databricks.com/product/automl) and many others.

Coming back to our experiment and model management discussion, although we covered the experiment part in the last post, we still haven’t discussed how to manage the models that we obtain as part of running our experiments. This is where [MLflow Model Registry](https://www.mlflow.org/docs/latest/model-registry.html) comes in.

### The Case for Model Registry

![](/img/1*qcLvbj7YfFQLkbm2FIk2Ew.jpeg)The idea of a Model Registry is quite similar to a General Ledger.As the processes to **create, manage** and **deploy** machine learning models evolve, organizations need to have a central platform that allows different personas such as **data scientists** and **machine learning engineers** to **collaborate, share code, artifacts** and **control** the stages of machine learning models. Breaking this down in terms of **functional requirements**, we are talking about the following desired capabilities:

* **discovering models**, visualizing experiment runs and the code associated with models
* **transitioning models** across different deployment stages, such as **Staging, Production** and **Archived**
* **deploying** different versions of a registered model in different stages, offering [Machine Learning engineers](https://www.techtarget.com/searchenterpriseai/definition/machine-learning-engineer-ML-engineer) and [MLOps](https://databricks.com/glossary/mlops) engineers the ability to deploy and conduct testing of different model versions (for instance, [A/B testing](https://en.wikipedia.org/wiki/A/B_testing), [Multi-Armed Bandits](https://en.wikipedia.org/wiki/Multi-armed_bandit) etc)
* **archiving** older models for **traceability** and **compliance** purposes
* **enriching** model **metadata** with **textual descriptions** and **tags**
* **managing authorization** and **governance** for model transitions and modifications with **access control lists (ACLs)**

![](/img/1*Veo7C6_7lZvJCaYaM0rWuA.jpeg)A typical MLOps Model Lifecycle using MLflow### Getting Started with MLflow Model Registry

Now to the practical part. We will run some code to train a model and showcase MLflow Model Registry capabilities. Hereby we present two possible options for running the notebooks from this quickstarter: you can choose to run them on Jupyter Notebooks with a local MLflow instance, or in a Databricks workspace.

**Jupyter Notebooks**

If you want to run these examples using [Jupyter Notebooks](https://jupyter.org/), please follow these steps:

* Clone this [Github repo](https://github.com/rafaelvp-db/mlflow-getting-started) to your local machine
* Make sure you are running **Python 3.8.7** (quick hint: you can run multiple Python versions on a single machine by installing [pyenv](https://github.com/pyenv/pyenv))
* Once you have a working Python 3.8.7 installation, create a virtual environment by running `python -m venv .venv`
* Configure your **virtual environment** by running `make env.` Alternatively, you can do it manually by running the following from the terminal:


```
export SYSTEM\_VERSION\_COMPAT=1 && \  
source .venv/bin/activate && \  
pip install --upgrade pip && \  
pip install wheel && \  
pip install -r requirements.txt && \  
pre-commit install
```
* Run the first notebook `jupyter/01_train_model.ipynb.` This will create an experiment and multiple runs with different hyperparameters for a diabetes prediction model.
* Run the second notebook `jupyter/02_register_model.ipynb.` By doing so, we will register our model artifact into MLflow model registry. We will also do some basic sanity checks in order to confirm that our model can be promoted to `Staging.`
* For this example we are running a simple, local instance of **MLflow** with a **SQLite** backend — which is good enough for a toy example, but not recommended for a test or production setup. It is also possible to run **MLflow** **locally** or **remotely** as a standalone web application, and also with a **Postgresql** backend. For more details on how to achieve this, please refer to the different scenarios presented in [this link.](https://www.mlflow.org/docs/latest/tracking.html)

**Databricks**

* Running the same code with [Databricks Managed MLflow](https://databricks.com/product/managed-mlflow) is even simpler, since the environment is already configured when you use an [LTS ML](https://docs.databricks.com/release-notes/runtime/10.4ml.html) cluster. Please make sure that you have such a cluster available, and then clone the [repo](https://github.com/rafaelvp-db/mlflow-getting-started) into your workspace. [For more details on Databricks integration with repos, please refer to this article.](https://docs.databricks.com/repos/index.html)
* Run the first notebook `databricks/01_train_model.py.`
* Run the second notebook `databricks/02_register_model.py.`
* **Bonus 1:** if you run these notebooks on a Databricks Workspace, you will be able to visualize the different runs associated with your experiment:

![](/img/1*JwO0h4pZUZGaD0kOh4FQLQ.png)MLflow Experiment window containing all of your experiment runs### Experiments, runs and models

Looking at the screenshot above, you might notice that on the first row of our table, in the **models** column, we have an **icon** which differs from the other rows. This is due to the fact that the **model artifact for that specific run** was **registered as a model**, and a new model version was created (version 1). If we click on its link, we get redirected to the following window.

![](/img/1*1JcZnkFaNOlLcM8xSJffOw.png)Model Registry window for the model version that we registered as part of notebook 2On the window above, we have an overview of the model version that was registered. We can see that it has the tag `prediction_works = true.` We can also see that it is in **Staging**. Depending on which persona is accessing this data, it might be possible to manually change the stage (to promote the model to Production, for instance), or reverting it back to None.

Moreover, with [Workspace Object Access Control Lists](https://docs.databricks.com/security/access-control/workspace-acl.html), you could limit the permissions for each type of user. Let’s say that you wish to block data scientists from transitioning model stages, while you want to allow team manager to do so. In such scenario, Data Scientists would have to **request transitions** to a given stage.

![](/img/1*FHX3RpF6vwA740J7nFYiHw.png)Stage transition request window in MLflow Model Registry (Databricks)These transitions would then need to be approved by someone with the right permissions. Finally, all of the requests and model stage transitions are tracked in the same window (and of course, they are also available programatically).

Once a model has been transitioned to **Production**, it is quite simple to deploy it either as an **automated job** or as a **Real time REST API Endpoint**. But that is the topic for another post.

All the code used in this post is available on the Github repo below:

[**GitHub - rafaelvp-db/mlflow-getting-started: A simple repo to get started with MLflow.**  
*TLDR; this repo contains some starter code in order to become familiar with MLflow Tracking and MLflow Model Registry.*github.com](https://github.com/rafaelvp-db/mlflow-getting-started "https://github.com/rafaelvp-db/mlflow-getting-started")### References

[**MLflow Model Registry**  
*If running your own MLflow server, you must use a database-backed backend store in order to access the model registry…*www.mlflow.org](https://www.mlflow.org/docs/latest/model-registry.html#api-workflow "https://www.mlflow.org/docs/latest/model-registry.html#api-workflow")[**Managed MLflow**  
*What is Managed MLflow? Managed MLflow is built on top of MLflow, an open source platform developed by Databricks to…*databricks.com](https://databricks.com/product/managed-mlflow "https://databricks.com/product/managed-mlflow")[**GitHub - mlflow/mlflow: Open source platform for the machine learning lifecycle**  
*MLflow is a platform to streamline machine learning development, including tracking experiments, packaging code into…*github.com](https://github.com/mlflow/mlflow/ "https://github.com/mlflow/mlflow/")[**MLflow Model Registry on Databricks**  
*Learn about the Model Registry in Databricks.*docs.databricks.com](https://docs.databricks.com/applications/mlflow/model-registry.html "https://docs.databricks.com/applications/mlflow/model-registry.html")

