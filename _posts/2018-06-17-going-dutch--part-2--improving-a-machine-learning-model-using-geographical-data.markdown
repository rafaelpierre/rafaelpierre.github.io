---
layout:	post
title:	"Going Dutch, Part 2: Improving a Machine Learning Model Using Geographical Data"
date:	2018-06-17
canonical_url: https://towardsdatascience.com/going-dutch-part-2-improving-a-machine-learning-model-using-geographical-data-a8492b67b885
---





---

![](/img/1*poYdKqzHObmAug8rLUuLWQ.jpeg)### Where it all Started

[In my previous post](https://towardsdatascience.com/going-dutch-how-i-used-data-science-and-machine-learning-to-find-an-apartment-in-amsterdam-part-def30d6799e4), I described the process of hunting for an **apartment** in **Amsterdam** using **Data Science** and **Machine Learning**. Using apartment rental data obtained from the internet, I was able to explore and visualize this data. As part of the visualization part I was able to create the map below:

Ultimately I was able to use this data to **build**, **train** and **test** a **predictive model** using **Random Forests**. It was possible to achieve an **R2** score of **0.70,** which is a good measure for a baseline model. The results in terms of predictions versus actual values for the test set can be seen in the plot below:

![](/img/1*m6f7RXtr8p4IS0h_yiP0YQ.png)The idea of creating a **predictive model** out of this data was to have a good parameter in order to know if a rental listing had a **fair price** or not. This would allow us to find some **bargains** or **distortions.** The **reasoning** behind this was that if I came across any apartment with a **rental price** that was **much lower** than a value **predicted by our model,** this could indicate a good deal. In the end, this proved to be an efficient way for house hunting in Amsterdam as I was able to focus on specific areas, detecting some good deals and finding an apartment within my first day in the city.

![](/img/1*ArRe2lRSGRHDRr4OT3PBVQ.gif)After finding an apartment in AMSNow going back to our model. Being a baseline model, there is potential room for improvement in terms of prediction quality. The pipeline below has become my favorite approach for tackling data problems:

1. Start out with a **baseline model**
2. Check the **results**
3. **Improve** the model
4. **Repeat** until the results are satisfactory

So here we are now, at step three. We need to improve our model. In the last post, I listed the reasons why I like **Random Forests** so much, one of them being the fact that you don’t need to spend a lot of time tuning **hyperparameters** (which is the case for **Neural Networks** for example). While this is a good thing, on the other hand it imposes us some limitations in order to improve our model. We are pretty much left with working and improving our data rather than trying to improve our predictive model by tweaking its parameters.

This is one of the beauties of **Data Science**. Sometimes it feels like an investigation job: you need to look for leads and connect the dots. It’s almost like *the truth is out there.*

![](/img/1*SWBZvc1QHAIXxCcm9VwWgA.png)Look! An empty apartment in Amsterdam!So now we know that we need to work on our data and make it better. But how?

In our original dataset, we were able to apply some feature engineering in order to create some variables related to the apartment location. We created dummy variables for some categorical features, such as **address** and **district**. This way we ended up creating one variable for each address and district category, their value being either 0 or 1. But there is one aspect that we missed in this analysis.

### Venice of the North

![](/img/1*FefzSKGHURX-BjaHzSli1A.jpeg)Amsterdam has more than one hundred kilometers of [*grachten*](https://en.wikipedia.org/wiki/Gracht "Gracht") ([canals](https://en.wikipedia.org/wiki/Canal "Canal")), about 90 islands and 1,500 bridges. Alongside the main canals are 1550 monumental buildings. The 17th-century canal ring area, including the Prinsengracht, Keizersgracht, Herengracht and Jordaan, were listed as UNESCO [World Heritage Site](https://en.wikipedia.org/wiki/World_Heritage_site "World Heritage site") in 2010, contributing to Amsterdam’s fame as the “[Venice of the North](https://en.wikipedia.org/wiki/Venice_of_the_North "Venice of the North")”.

![](/img/1*9NmEYY8wZCzooLLqmWPQXA.jpeg)The **addresses** in Amsterdam usually contain information which allows one to know if a place sits in front of a canal or not — the so called “*canal houses*”. An apartment located at **Leidsegracht** most likely has a view to the canal, while the same cannot be said for an apartment located at **Leidsestraat,** for instance.There are also cases where buildings are located within a square, for example some buldings at **Leidseplein**.

Needless to say, canal houses have an extra appeal due to the beautiful view they provide. In Facebook groups it is possible to see canal houses being rented in the matter of hours after being listed.

![](/img/1*j2TlqBnTpDTWj23jwQn4pA.jpeg)Who wants to live in a Canal House?We will extract this information from the apartments addresses in order to create three more variables: *gracht*, *straat* and *plein*, with 0 and 1 as possible values.The reason for creating separate variables for these instead of only one with different possible values (e.g. 1,2,3) is that in this case we would treat it as a continuous variable, tricking our model into considering this scale for means of importance. We will hopefully find out if canal houses are really that sought for.

### Location, Location, Location

By observing the top 15 most important features from our model’s **Feature Importance** ranking, we are able to notice that besides **latitude** and **longitude**, many of the dummy variables related to **address** and **district** are valuable for our model in order to properly do its predictions. So we can say that location data is definitely promising.

We will expand on that. But again, the question is, how?

![](/img/1*6nK8SpUSQXcQzOrVpk1EAg.jpeg)Restaurants, bars and cafes near Leidseplein, Amsterdam.### Going Social

Besides having around 800K inhabitants — a small number when it comes to Western Europe capitals — Amsterdam is packed with bars, cafes, restaurants and has one of the best public transportation systems in Europe. However, it is important to think about our target subject: **people**. Our main objective here is *understanding how people behave when looking for an apartment*. We need to segregate our target into different groups, in a way that we can understand what they want in terms of housing and location. One could argue that being close to bars, cafes and restaurants is attractive for some kinds of people. Other people could be willing to live closer to parks and schools — couples with small kids, for example. Both types of people could also be interested in living close to public transportation, such as Tram and Bus stops.

![](/img/1*Ie0A5arVRc5MqlEXyH_zgQ.jpeg)Amsterdam Centraal StationThis gives us some hints on formulating our hypothesis. Would proximity to these types of places impact apartment rental prices?

In order to test this hypothesis, we need to feed this data into our model.

[Yelp](https://www.yelp.com) is a social platform that advertises its purpose as “*to connect people with great local businesses”*. It lists spots such as bars, restaurants, schools and lots of other types of POI — *points of interest* throughout the world, allowing users to write reviews for places. Yelp had a monthly average of 30 million unique visitors who visited Yelp via the Yelp app and 70 million unique visitors who visited Yelp via mobile web in Q1 2018. Through Yelp’s [Fusion API](https://www.yelp.com/developers/documentation/v3) one can easily extract POI information passing latitude and longitude as parameters.

Yelp has some categories for places listed on its database (unfortunately, there is no category for *coffeeshop*). We are interested in the following:

**Active Life**: parks, gyms, tennis courts, basketball courts

**Bar**: bars and pubs

**Cafe**: self-explanatory

**Education**: kindergarten, high schools and universities

**Hotels/Travel**: hotels, car rental shops, touristic information points

**Transportation**: tram/bus stops and metro stations

For each of these categories, Yelp lists POI containing their latitude and longitude.

Our approach here will be:

1. **Querying** the **Yelp Fusion API** in order to get data on POI for the categories above in Amsterdam
2. **Calculating** the distance in meters between each **apartment** and each **POI**.
3. **Counting** how many **POIs** from each category are within a **250 meters radius** from each of the **apartments**. These numbers will become variables in our dataset.

![](/img/1*66H_XkIUrWB_-jH04rDvcw.png)By using Yelp’s Fusion API we have been able to grab geographic data on 50 POI for each of the categories that are within our target.

Before we proceed to calculating the distance between each POI and each apartment, remember: **Latitude** and **Longitude** are **angle** measures.

**Latitude** is measured as the degrees to the north or south of the [Equator](https://en.wikipedia.org/wiki/Equator). **Longitude** is measured as the degrees to the east or west of the [Prime Meridian (or Greenwich) line](https://en.wikipedia.org/wiki/Prime_meridian_%28Greenwich%29). The combination of these two angles can be used to pinpoint an exact location on the surface of the earth.

![](/img/1*Z-mWIMVFrrnkWZYDcmRkwg.png)As shown in the image above, the quickest route between two points on the surface of the earth is a “[great circle path](https://en.wikipedia.org/wiki/Great_circle)” — in other words, a path that comprises a part of the longest circle you could draw around the globe that intersects the two points. And, since this is a circular path on a sphere using coordinates expressed in angles, all of the properties of the distance will be given by trigonometric formulas.

![](/img/1*nnK3W0OPUv1YPzttQzOc8w.png)Haversine Formula.The shortest distance between two points on the globe can be calculated using the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula). In Python, it would look like this:


```
from math import sin, cos, sqrt, atan2, radians  
  
# approximate radius of earth in km  
R = 6373.0  
  
lat1 = radians(52.2296756)  
lon1 = radians(21.0122287)  
lat2 = radians(52.406374)  
lon2 = radians(16.9251681)  
  
dlon = lon2 - lon1  
dlat = lat2 - lat1  
  
a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2  
c = 2 * atan2(sqrt(a), sqrt(1 - a))  
  
distance = R * c
```
Now that we know how to calculate the distance between two points, for each apartment we will count how many POI from each of the categories are within a 250 meters radius.

After concatenating this data into our previous dataset, let’s have a glimpse at how it looks — notice the last columns on the right side:

![](/img/1*SDxlzbFggW-PjTLZerkLcA.png)### Putting it all Together

Let’s take a look at our dataset after adding these variables.

We’ll start out by getting some measures for descriptive statistics:

![](/img/1*b-BXx95wyg46S5Pq9t3ZqA.png)* Apartments have an average 0.7828 **bars** within 250 meters radius. Good news for those who like to go for a beer without walking (or tramming) too much.
* **Cafes** also seem to be widely spread across the city, with an average 0.6703 POI within walking distance from each apartment.
* The average quantity of **transportation** POI within 250 meters of apartments is close to zero.

We’ll now generate some **boxplots** for these variables and see how they influence **normalized\_price**.

![](/img/1*R58HVfI0LMLZcGMdJRTzIA.png)It looks like these three variables indeed have significant influence over **normalized\_price**.

What about **gracht**, **straat** and **plein**?

![](/img/1*YS0ChbOXtMwhhfY3uo0bdQ.png)As expected, prices are slightly higher for **canal houses** (gracht) and also for apartments located in **squares** (plein). For apartments located in regular streets, prices are slightly lower.

Now we’ll wrap everything up and generate a heatmap through the **Pearson Correlation** matrix between the new variables we introduced in the model and our target variable, **normalized\_price**.

![](/img/1*v38zsuW3i_Vh4j2o44hgBg.png)Unfortunately, our **heatmap** does not provide any indication of significant correlation between our new variables and **normalized\_price**. But again, that doesn’t mean there is no relationship **at all** between them, it just means there is no significant **linear** relationship.

### Going Green, Part 2

Now that we enriched our dataset, it’s time to train our model with the new data and see how it performs.

![](/img/1*DMLw9TqISirh7CxH_Bifeg.png)How our new predictions perform. Predicted values in orange, actual values in blue.We were able to increase our **R2 Score** from **0.70** to **0.75 —**around **7.14%** improvement considering our baseline model.

The plot above depicts the new predicted values we obtained in comparison with the actual ones. It is possible to see a small improvement specially for predicting values close to the maximum and minimum prices.

In terms of feature importances, something interesting occurred. Some of the new variables that we introduced gained substantial importance, thus removing importance from other variables. Notice how the dummy variables generated by the **address** variable lost importance. In the case of the **district** variables, they are not even part of the top 15 most important variables anymore. Probably we wouldn’t see much difference in our results should we want to remove these variables from our model.

It is also interesting to note that the quantity of transportation POI within a 250 meters radius is not as important as the quantity of cafes within this distance. One possible guess is that transportation is more homogeneously dispersed through the city — most apartments would be close to trams, bus or metro stops, while cafes might be concentrated in more central areas.

We explored much of the geographic data available. Perhaps a way to make our model even better would be getting information such as building construction date, apartment conditions and other characteristics. We could even play a bit with the geographic data and base our variables in a greater radius than 250 meters for POI. It is also possible to explore other Yelp categories such as shops, grocery stores, among many others and see how they affect rental prices.

### Key Takeaways

* Improving a model’s prediction capacity is not a trivial task and may require a bit of creativity to find ways of making our data richer and more comprehensive
* Sometimes a small model improvement requires a decent amount of work
* In the predictive analytics pipeline, obtaining, understanding, cleaning and enriching your data is a critical step which is sometimes overlooked; it is also the most time consuming task — and in this case, it was also the most fun part

This is **Part 2** of a two parts series. Check out **Part 1** here:

[**Going Dutch: How I Used Data Science and Machine Learning to Find an Apartment in Amsterdam — Part…**  
*Amsterdam’s Real Estate Market is experiencing an incredible ressurgence, with property prices soaring by double-digits…*towardsdatascience.com](https://towardsdatascience.com/going-dutch-how-i-used-data-science-and-machine-learning-to-find-an-apartment-in-amsterdam-part-def30d6799e4 "https://towardsdatascience.com/going-dutch-how-i-used-data-science-and-machine-learning-to-find-an-apartment-in-amsterdam-part-def30d6799e4")If you liked this post, you might also enjoy these:

[**Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 1**  
*Learn why Model Tracking and MLflow are critical for a successful machine learning project*mlopshowto.com](https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-1-f8ca857b5971 "https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-1-f8ca857b5971")[**Detecting Financial Fraud Using Machine Learning: Winning the War Against Imbalanced Data**  
*Would Machine Learning and AI constitute great allies in this battle?*towardsdatascience.com](https://towardsdatascience.com/detecting-financial-fraud-using-machine-learning-three-ways-of-winning-the-war-against-imbalanced-a03f8815cce9 "https://towardsdatascience.com/detecting-financial-fraud-using-machine-learning-three-ways-of-winning-the-war-against-imbalanced-a03f8815cce9")

