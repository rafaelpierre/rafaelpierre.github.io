---
layout:	post
title:	"Data Pipeline Orchestration on Steroids: Getting Started with Apache Airflow, Part 1"
date:	2020-06-27
canonical_url: https://mlopshowto.com/data-pipeline-orchestration-on-steroids-getting-started-with-apache-airflow-part-1-22b503036ee
---





---

![](/img/1*lFms-VsbFgQBh51ppqcbTQ.jpeg)[Source: Unsplash](https://unsplash.com/photos/6DBZqMe2c5U)### What is Apache Airflow?

![](/img/1*17GV50mJaUWc1445A2h_QA.jpeg)[Source: Unsplash](https://unsplash.com/photos/xNdPWGJ6UCQ)**Apache Airflow** is an **open source** data workflow management project originally created at **AirBnb** in 2014. In terms of data workflows it covers, we can think about the following sample use cases:

🚀 Automate Training, Testing and Deploying a Machine Learning Model

🍽 Ingesting Data from Multiple REST APIs

🚦 [Coordinating Extraction, Transformation and Loading (ETL) or Extraction, Loading and Transformation (ELT) Processes Across an Enterprise Data Lake](https://www.qubole.com/blog/apache-airflow-tutorial-etl-elt-workflow-orchestration-made-easy/)

As we can see, one of the main features of Airflow is its flexibility: it can be used for many different data workflow scenarios. Due to this aspect and to its rich feature set, it has gained significant traction over the years, having been battle tested in many companies, from **startups** to **Fortune 500** enterprises. Some examples include **Spotify, Twitter, Walmart, Slack, Robinhood, Reddit, PayPal, Lyft, and of course, AirBnb**.

### OK, But Why?

#### Feature Set

* **Apache Airflow** works with the concept of [**Directed Acyclic Graphs (DAGs)**](https://en.wikipedia.org/wiki/Directed_acyclic_graph)**,** which are a powerful way of defining dependencies across different types of tasks. In **Apache Airflow**, DAGs are developed in **Python**, which unlocks many interesting features from software engineering: **modularity, reusability, readability**, among others.

![](/img/1*_whkfbqHtz1AnhpbBTJiQw.png)[Source: Apache Airflow Documentation](https://airflow.apache.org/docs/stable/concepts.html)* [**Sensors**](https://www.xplenty.com/blog/apache-airflow-explained/#sensors)**,** [**Hooks**](https://airflow.apache.org/docs/stable/concepts.html?highlight=hook#hooks)and [**Operators**](https://airflow.apache.org/docs/stable/concepts.html?highlight=hook#operators)are the main building blocks of **Apache Airflow.** They provide an easy and flexible way of connecting to multiple external resources. Want to integrate with **Amazon S3**? Maybe you also want to add **Azure Container Instances** to the picture in order to run some short-lived **Docker** containers? Perhaps running a batch workload in an **Apache Spark** or **Databricks** cluster? Or maybe just executing some basic **Python** code to connect with **REST APIs**? Airflow ships with multiple operators, hooks and sensors out of the box, which allow for easy integration with these resources, and many more, such as: [**DockerOperator**](https://airflow.apache.org/docs/stable/_api/airflow/operators/docker_operator/index.html), [**BashOperator**](https://airflow.apache.org/docs/stable/_api/airflow/operators/bash_operator/index.html), [**HiveOperator**](https://airflow.apache.org/docs/stable/_api/airflow/operators/hive_operator/index.html), [**JDBCOperator**](https://airflow.apache.org/docs/stable/_api/airflow/operators/jdbc_operator/index.html)— [the list goes on](https://airflow.apache.org/docs/stable/_api/airflow/operators/index.html).You can also build upon one of the standard operators and create your own. Or you can simply write your own operators, hooks and sensors from scratch.
* The **UI** allows for quick and easy **monitoring** and **management** of your Airflow instance. Detailed logs also make it easier to debug your **DAGs**.

![](/img/1*JR82-8vVaYOstcrGLbXX_A.png)Airflow UI Tree View. Source: [Airflow Documentation](https://airflow.apache.org/docs/stable/ui.html)…and there are many more. Personally, I believe one of the fun parts of working with Airflow is discovering new and exciting features as you use it — and if you miss something, you might as well create it.

* It is part of the **Apache Foundation**, and the community behind it is pretty active — currently there are more than a hundred [direct contributors](https://github.com/apache/airflow/graphs/contributors). One might argue that Open Source projects always run the risk of dying at some point — but with a vibrant developer community we can say this risk is mitigated. In fact, 2020 has seen individual contributions for Airflow at an all-time high.

### Apache Airflow Tutorial

Time to get our hands dirty and actually start with the tutorial.

There are multiple ways of installing Apache Airflow. In this introduction we will cover the easiest one, which is by installing it from the **PyPi** repository.

#### Basic Requirements

* **Python 3.6+**
* **Pip**
* **Linux/Mac OS** — for those running **Windows**, activate and install[**Windows Subsystem for Linux (WSL)**](https://docs.microsoft.com/en-us/windows/wsl/install-win10)**,** download **Ubuntu 18 LTS** from the Windows Marketplace and be happy :)

#### Initial Setup

* Create a new directory for your Airflow project (e.g. “*airflow-intro*”)
* From your new directory, create and activate a new virtual environment for your Airflow project using **venv**


```
# Run this from newly created directory to create the venv  
python3 -m venv venv
```

```
# Activate your venv  
source venv/bin/activate
```
* Install **apache-airflow** through pip


```
pip install apache-airflow
```
Before proceeding, it is important to discuss a bit about Airflow’s main component: the [**Executor**](https://airflow.apache.org/docs/stable/executor/index.html). The name is pretty self-explanatory: this component handles the **coordination** and **execution** of different **tasks** across multiple **DAGs**.

There are many types of **Executors** in **Apache Airflow,** such as the **SequentialExecutor**, **LocalExecutor**, **CeleryExecutor**, **DaskExecutor** and others. For the sake of this tutorial, we will focus on the **SequentialExecutor**. It presents very basic functionality and has a main limitation, which is the fact that it cannot execute tasks in parallel. This is due to the fact that it leverages a [**SQLite**](https://www.sqlite.org/index.html) database as the backend (which can only handle one connection at a time), hence [multithreading](https://en.wikipedia.org/wiki/Multithreading_%28computer_architecture%29#:~:text=In%20computer%20architecture%2C%20multithreading%20is,This%20approach%20differs%20from%20multiprocessing.) is not supported. Therefore it is not recommended for a **Production** setup, but it should not be an issue for our case.

Going back to our example, we need to initialize our backend database. But before that, we must override our AIRFLOW\_HOME environment variable, so that we specify that our current directory will be used for running Airflow.


```
export AIRFLOW\_HOME=$(pwd)
```
Now we can initialize our Airflow database. We can do this by simply executing the following:


```
airflow initdb
```
Take a look at the output and make sure that no error messages are displayed. If everything went well, you should now see the following files in your directory:

![](/img/1*GY49jaqJhVNLK0ZznQ998g.png)* To confirm if the initialization is correct, quickly inspect **airflow.cfg** and confirm if the following lines correctly point to your work directory in the [core] section. If they do, you should be good to go.

![](/img/1*O1U8mhDvF2vRRppP-nWywg.png)**Optional**: Airflow ships with many sample DAGs, which might help you get up to speed with how they work. While it is certainly helpful, it can make your UI convoluted. You can set **load\_examples** to **False**, so that you will see only your own DAGs in the Airflow’s UI.

#### DAG Creation

We will start with a really basic DAG, which will do two simple tasks:

1. Create a text file
2. Rename this text file

To get started, create a new **Python** script file named **simple\_bash\_dag.py** inside your dags folder. In this script, we must first import some modules:


```
# Python standard modules  
from datetime import datetime, timedelta
```

```
# Airflow modules  
from airflow import DAG  
from airflow.operators.bash\_operator import BashOperator
```
We now proceed to creating a DAG object. In order to do that, we must specify some basic parameters, such as: when will it become active, which intervals do we want it to run, how many retries should be made in case any of its tasks fail, and others. So let’s define these parameters:


```
default\_args = {  
    'owner': 'airflow',  
    'depends\_on\_past': False,  
    # Start on 27th of June, 2020  
    'start\_date': datetime(2020, 6, 27),  
    'email': ['airflow@example.com'],  
    'email\_on\_failure': False,  
    'email\_on\_retry': False,  
    # In case of errors, do one retry  
    'retries': 1,  
    # Do the retry with 30 seconds delay after the error  
    'retry\_delay': timedelta(seconds=30),  
    # Run once every 15 minutes  
    'schedule\_interval': '\*/15 \* \* \* \*'  
}
```
We have defined our parameters. Now it is time to actually tell our DAG what it is supposed to do. We do this by declaring different tasks — T1 and T2. We must also define which task depends on the other.


```
with DAG(
```

```
    dag\_id=’simple\_bash\_dag’,  
    default\_args=default\_args,  
    schedule\_interval=None,  
    tags=[‘my\_dags’],  
) as dag:
```

```
    #Here we define our first task  
    t1 = BashOperator(bash\_command=”touch ~/my\_bash\_file.txt”, task\_id=”create\_file”)
```

```
    #Here we define our second task  
    t2 = BashOperator(bash\_command=”mv ~/my\_bash\_file.txt ~/my\_bash\_file\_changed.txt”, task\_id=”change\_file\_name”)
```

```
    # Configure T2 to be dependent on T1’s execution  
    t1 >> t2
```
And as simple as that, we have finished creating our DAG 🎉

#### Testing our DAG

Let’s see how our DAG looks like and most importantly, see if it works.

To do this, we must start two Airflow components:

* The **Scheduler**, which controls the flow of our DAGs


```
airflow scheduler
```
* The **Web Server**, an UI which allows us to control and monitor our DAGs


```
airflow webserver
```
You should see the following outputs (or at least something similar):

![](/img/1*wl5tjUmiSSMx54nwcaPukw.png)Output for the Scheduler’s startup![](/img/1*GZdgcjOvuIS3ZbpcYCgOrQ.png)Output for the Webserver’s startup#### Showtime

We should now be ready to look at our Airflow UI and test our DAG.

Just fire up your navigator and go to <https://localhost:8080.> Once you hit Enter, the Airflow UI should be displayed.

![](/img/1*JEB4t361WRMDWORJ7PG1Ug.png)Look for our DAG — *simple\_bash\_dag —* and click on the button to its left, so that it is activated. Last, on the right hand side, click on the play button ▶ to trigger the DAG manually.

Clicking on the DAG enables us to see the status of the latest runs. If we click on the **Graph View**, we should see a graphical representation of our DAG — along with the color codes indicating the execution status for each task.

![](/img/1*6QlYkpwNa2zRsIVqoWpWLw.png)As we can see, our DAG has run successfully 🍾

We can also confirm that by looking at our home directory:

![](/img/1*1D2YrWlTzBn7OsVHP8qRRA.png)### Wrap Up

* We had a quick **tutorial** about **Apache Airflow**, how it is used in different companies and how it can help us in setting up different types of data pipelines
* We were able to install, setup and run a simple **Airflow** environment using a **SQLite** backend and the **SequentialExecutor**
* We used the **BashOperator** to run simple file creation and manipulation logic

There are many nice things you can do with Apache Airflow, and I hope my post helped you get started. If you have any questions or suggestions, feel free to comment.

You might also like some of my other stories:

[**Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 2**  
*Learn how to use MLflow Model Registry to track, register and deploy Machine Learning Models effectively.*mlopshowto.com](https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc "https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc")[**Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 1**  
*Learn why Model Tracking and MLflow are critical for a successful machine learning project*mlopshowto.com](https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-1-f8ca857b5971 "https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-1-f8ca857b5971")[**An Apache Airflow MVP: Complete Guide for a Basic Production Installation Using LocalExecutor**  
*Simple and quick way to bootstrap Airflow in production*towardsdatascience.co](https://towardsdatascience.com/an-apache-airflow-mvp-complete-guide-for-a-basic-production-installation-using-localexecutor-beb10e4886b2 "https://towardsdatascience.com/an-apache-airflow-mvp-complete-guide-for-a-basic-production-installation-using-localexecutor-beb10e4886b2")

