---
layout:	post
title:	"Detecting Financial Fraud Using Machine Learning: Winning the War Against Imbalanced Data"
date:	2018-06-27
canonical_url: https://mlopshowto.com/detecting-financial-fraud-using-machine-learning-three-ways-of-winning-the-war-against-imbalanced-a03f8815cce9
---



The main challenge when it comes to modeling fraud detection as a classification problem comes from the fact that the majority of transactions is not fraudulent, making it hard to train an ML model.




---

![](/img/1*uke4skoetttEBQDJwnae8g.png)For years, fraudsters would simply take numbers from **credit** or **debit cards** and print them onto blank plastic cards to use at brick-and-mortar stores. But in 2015, **Visa** and **Mastercard** mandated that banks and merchants introduce **EMV** — [chip card technology](https://en.wikipedia.org/wiki/EMV), which made it possible for merchants to start requesting a PIN for each transaction.

Nevertheless, [experts predict online credit card fraud to soar](https://nilsonreport.com/upload/content_promo/The_Nilson_Report_10-17-2016.pdf) to a whopping **$32 billion** in 2020.

Putting it into perspective, this amount is superior to the profits posted recently by some worldwide household, blue chip companies in 2017, such as **Coca-Cola** ($2 billions), Warren Buffet’s **Berkshire Hathaway** ($24 billions) and **JP Morgan Chase** ($23.5 billions).

In addition to the implementation of chip card technology, companies have been investing massive amounts in other technologies for detecting fraudulent transactions.

Would **Machine Learning & AI** constitute great allies in this battle?

### Classification Problems

![](/img/1*4vnglpUYwoluB9jxI845gQ.png)In **Machine Learning**, problems like fraud detection are usually framed as **classification problems —**predicting a discrete class label output given a data observation. Examples of classification problems that can be thought of are **Spam Detectors**, **Recommender Systems** and **Loan Default Prediction**.

Talking about the credit card payment fraud detection, the classification problem involves creating models that have enough intelligence in order to properly classify transactions as either **legit** or **fraudulent**, based on transaction details such as **amount, merchant, location, time** and others.

Financial fraud still amounts for considerable amounts of money. Hackers and crooks around the world are always looking into new ways of committing financial fraud at each minute. Relying exclusively on rule-based, conventionally programmed systems for detecting financial fraud would not provide the appropriate time-to-market. This is where **Machine Learning** shines as a unique solution for this type of problem.

The main challenge when it comes to modeling fraud detection as a classification problem comes from the fact that in real world data, the majority of transactions is not fraudulent. Investment in technology for fraud detection has increased over the years so this shouldn’t be a surprise, but this brings us a problem: **imbalanced data**.

### Imbalanced Data

![](/img/1*faPNdX0gzoHQViOBhrYLcA.jpeg)Imagine that you are a teacher. The school director gives you the task of generating a report with predictions for each of the students’ final year result: **pass** or **fail**. You’re supposed to come up with these predictions by analyzing student data from previous years: **grades**, **absences**, **engagement** together with the **final result,** the target variable — which could be either **pass** or **fail**. You must submit your report in some minutes.

The “problem” here is that you are a very good teacher. As a result, almost none of your past students has failed your classes. Let’s say that **99%** of your students have passed final year exams.

What would you do?

The most **fast**, **straightforward** way to proceed in this case would be predicting that **100% of all your students would pass**. **Accuracy** in this case would be **99%** when simulating past years. Not bad, right?

This happens when we have imbalance.Would this “*model*” be correct and fault proof regardless of characteristics from all your future student populations?

Certainly not. Perhaps you wouldn’t even need a teacher to do these predictions, as anyone could simply try guessing that the whole class would pass based on data from previous years, and still achieve a good accuracy rate. Bottomline is that *this prediction would have no value*. And one of the most important missions of a **Data Scientist** is *creating business value out of data*.

We’ll take a look into a practical case of fraud detection and learn how to overcome the issue with imbalanced data.

### Our Data

![](/img/1*o0xTlKG8AHgnXfVh36X-6A.jpeg)Our dataset contains transactions made by **credit cards** in September 2013 by european cardholders. This dataset presents transactions that occurred in two days, where we have **492 frauds** out of **284,807 transactions**. The dataset is highly **imbalanced**, with the positive class (frauds) accounting for **0.172%** of all transactions.

![](/img/1*oQidylKOUwrHsHZowsoVag.png)First 5 observations from our data, showing the first 10 variables.It is important to note that due to confidentiality reasons, the data was anonymized — variable names were renamed to V1, V2, V3 until V28. Moreover, most of it was scaled, except for the **Amount** and **Class** variables**,** the latter being our binary, target variable.

It’s always good to do some **EDA — Exploratory Data Analysis** before getting our hands dirty with our prediction models and analysis. But since this is an unique case where most variables add no context, as they’ve been anonymized, we’ll skip directly to our problem: dealing with **imbalanced data**.

![](/img/1*-by807a2zxPHB7_7RNDVtQ.png)Only 0.17% of our data is positively labeled (fraud).There are many ways of dealing with imbalanced data. We will focus in the following approaches:

1. Oversampling — **SMOTE**
2. Undersampling — **RandomUnderSampler**
3. Combined Class Methods — **SMOTE + ENN**

### Approach 1: Oversampling

One popular way to deal with imbalanced data is by **oversampling**. To oversample means to artificially create observations in our data set belonging to the class that is under represented in our data.

One common technique is **SMOTE** **— Synthetic Minority Over-sampling Technique**. At a high level, SMOTE creates synthetic observations of the minority class (in this case, fraudulent transactions). At a lower level, SMOTE performs the following steps:

* Finding the [k-nearest-neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) for minority class observations (finding similar observations)
* Randomly choosing one of the k-nearest-neighbors and using it to create a similar, but randomly tweaked, new observations.

There are many SMOTE implementations out there. In our case, we will leverage the SMOTE class from the **imblearn** library. The **imblearn** library is a really useful toolbox for dealing with imbalanced data problems.

To learn more about the SMOTE technique, [you can check out this link.](http://www.jair.org/papers/paper953.html)

### Approach 2: Undersampling

Undersampling works by sampling the dominant class to reduce the number of samples. One simple way of **undersampling** is randomly selecting a handful of samples from the class that is overrepresented.

The **RandomUnderSampler** class from the **imblearn** library is a fast and easy way to balance the data by randomly selecting a subset of data for the targeted classes. It works by performing [**k-means clustering**](https://en.wikipedia.org/wiki/K-means_clustering) on the majority class and removing data points from high-density centroids.

### Approach 3: Combined Class Method

SMOTE can generate noisy samples by interpolating new points between marginal outliers and inliers. This issue can be solved by cleaning the resulted space obtained after over-sampling.

In this regard, we will use **SMOTE** together with **edited nearest-neighbours** **(ENN).** Here, ENN is used as the cleaning method after SMOTE over-sampling to obtain a cleaner space. This is something that is easily achievable by using imblearn’s **SMOTEENN** class.

### Initial Results

Our model uses a **Random Forests Classifier** in order to predict fraudulent transactions. Without doing anything to tackle the issue of imbalanced data, our model was able to achieve **100% precision** for the **negative class** label.

This was expected since we’re dealing with imbalanced data, so for the model it’s easy to notice that predicting everything as negative class will reduce the error.

![](/img/1*C3JV6UQfKrv3EhdEFxqJHw.png)We have some good results for **precision**, considering both classes. However, **recall** is not as good as precision for the positive class (fraud).

Let’s add one more dimension to our analysis and check the **Area Under the Receiver-Operating Characteristic (AUROC)** metric. Intuitively, **AUROC** represents the likelihood of your model distinguishing observations from two classes. In other words, if you randomly select one observation from each class, what’s the probability that your model will be able to “*rank*” them correctly?

![](/img/1*s-XhvqUUiPvxr5L6NifOsQ.png)Our **AUROC** score is already pretty decent. Were we able to improve it even further?

### So, Have We Won?

After using **oversampling**, **undersampling** and **combined class** approaches for dealing with imbalanced data, we got the following results.

* **SMOTE**

![](/img/1*xHeCvYEo8ay13IXQ6lMiDA.png)By using **SMOTE** in order to oversample our data, we got some mixed results. We were able to improve our recall for the positive class by **5%** — we reduced false negatives. However, that came with a price: our precision is now **5%** worse than before. It is common to have a precision — recall trade-off in Machine Learning. In this specific case, it is important to analyze how would this impact us financially.

In one side, we would have reduced the amount of **false negatives.** On the other side, due to the increase in **false positives,** we would be potentially losing clients due to wrongfully classifying transactions as fraud, as well as increasing **operational costs** for cancelling credit cards, printing new ones and posting them to the clients.

In terms of **AUROC**, we got a slightly better score:

![](/img/1*N2pH7EIXjzJhGAoRUNC6YQ.png)* **RandomUnderSampler**

**Undersampling** proved to be a bad approach for this problem. While our recall score has improved, precision for the positive class has almost vanished.

![](/img/1*db4uiT5kTD0JiZ8iKILnaw.png)The results above show us that it wouldn’t be a good strategy to use **undersampling** for dealing with our imbalanced data problem.

* **SMOTE + ENN**

![](/img/1*UVQQR0XbiVPC5m3t8MdLUA.png)**SMOTE + ENN** proved to be the best approach in our scenario. While precision was penalized by **5%** like with **SMOTE**, our recall score was increased by **7%.**

As for the **AUROC** metric, the result was also better:

![](/img/1*Y3PUC2xZuYw8UBWlocuCDA.png)### Recap

In this post, I showed three different approaches to deal with imbalanced data — all of the leveraging the **imblearn** library:

1. **Oversampling** (using SMOTE)
2. **Undersampling** (using RandomUnderSampler)
3. **Combined Approach** (using SMOTE+ENN)

### Key Takeaways

* **Imbalanced data** can be a serious problem for building predictive models, as it can affect our prediction capabilities and mask the fact that our model is not doing so good
* **Imblearn** provides some great functionality for dealing with imbalanced data
* Depending on your data, **SMOTE**, **RandomUnderSampler** or **SMOTE + ENN** techniques could be used. Each approach is different and it is really the matter of understanding which of them makes more sense for your situation.
* It is important considering the trade-off between **precision** and **recall** and deciding accordingly which of them to prioritize when possible, considering possible business outcomes.

### You Might Also Like

[**Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 2**  
*Learn how to use MLflow Model Registry to track, register and deploy Machine Learning Models effectively.*mlopshowto.com](https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc "https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc")[**About MLOps And Why Most Machine Learning Projects Fail — Part 1**  
*If you have been involved with Machine Learning (or you are aiming to be), you might be aware that reaping the…*mlopshowto.com](https://mlopshowto.com/about-mlops-and-why-most-machine-learning-projects-fail-part-1-6a4d76e84e86 "https://mlopshowto.com/about-mlops-and-why-most-machine-learning-projects-fail-part-1-6a4d76e84e86")[**Data Pipeline Orchestration on Steroids: Getting Started with Apache Airflow, Part 1**  
*What is Apache Airflow?*towardsdatascience.com](https://towardsdatascience.com/data-pipeline-orchestration-on-steroids-getting-started-with-apache-airflow-part-1-22b503036ee "https://towardsdatascience.com/data-pipeline-orchestration-on-steroids-getting-started-with-apache-airflow-part-1-22b503036ee")### References

1. Nick Becker — [The Right Way to Oversample in Predictive Modelling](https://beckernick.github.io/oversampling-modeling/)
2. Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson and Gianluca Bontempi. *Calibrating Probability with Undersampling for Unbalanced Classification*. In Symposium on Computational Intelligence and Data Mining (CIDM), IEEE, 2015


