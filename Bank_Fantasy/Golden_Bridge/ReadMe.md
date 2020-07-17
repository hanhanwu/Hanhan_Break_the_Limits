# Bank Fantasy - Golden Bridge

<p align="center">
<img src="https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/imgs/golden_triangle.png" width="600" height="300" />
</p>

## Prototype
* [Click Me ❣][1]
* Benefits 💝💝
  * Helps small or medium business more, the bridge might also strength the community bonds
  * It helps promoting online contactless payment
  * Doesn't use individual user's identity data, proivacy with intelligence
  * Grow acceptance of digital payment
  * Address new payments flows

## Implementation
### Data Preprocessing
* `merchant_order.pkl` - Merchant Order table
  * It records detailed orders for each merchant
* `merchant_product.pkl` - Merchant Product table
  * It records the products selled by each merchant
* `ts_purchase.pkl` - Time Series table
  * It records daily purchase $ and clients amount for each merchant, used for later time series analysis, forecasting
* NOTE: Because of the limitation from online grocery data, there is some mockup data generated using monte carlo simulation. Such as merchant, price, purchase date. For the purpose of simplification, it also assume the sales prices for the same products is the same for each merchant.
* [My Code][2]💖
  * Correct - in `ts_purchase` table, clients daily count doesn't need to drop duplicates.

### Forecasting Preparation
* The main purpose of this section is to prepare for representative sample data, and choose a forecasting method that can be shared by the merchants.
* [My Code - Preparing for the sample datasets][3]💖
  * The 2 samples are representative to show 2 major types of time series curves.
  * "client_count" and "purchase_amount" are showing almost the same pattern in the curves. So in the forecasting experiemnts below, I will just use one of them.
* [My Code - Seasonal Decomposing][4]💖
  * I'm using Additive and Multiplicative methods to decopmpose the trend & season out, in order to observe how random the residuals are for both samples.
  * For sample 1, multiplicative residuals looks more random (better), for sample 2, not sure.
  * Residuals might not be stationary even though the trend and the season had been decomposed. Meanwhile, while the original time series doesn't have any null value, residuals will bring in null values. Residuals also have quite differnt value scale as the original time series, so currently, I'm not sure using residuals or (preprocessed) original time series is better for later forecasting.
  * Next, I'm going to do stationary analysis on different residuals, and also compare with the original data.
* [My Code - Stationary Analysis][5]💖
  * Through the stationary analysis on 2 representative samples, using original time series, processed time series, residuals and processed residuals. An easier solution is to use logged moving average of original time series, which is showing 90+% confidence of strict stationary in both samples.
  * So next, I'm going to calculate forecastability of the same sets of time series, just to compare. Even though it's highly likely that I will use logged moving average for forecasting.
* [My Code - Forecastable Analysis][6]💖
  * Same as Stationary Analysis, among all the used time series sequences, logged moving average from the original data still appear to be better than other choices, when it comes to forecastable analysis. Same for both sample data.
  * Next I'm going to use logged moving average to experiment on different forecasting methods to compare.
  
### Forecasting Experiments
* [My Code - Forecast Experiments - Fixed Window Solution][7]💖
  * The purpose in these experiments is to find whether there is an algorithm works better for all the samples here.
  * The training data is using all the historical data, instead of the latest historical data, this is why it's called "fixed window solution".
  * I was using the 2 representative samples, using their logged and logged moving average formats.
    * Because logged data still keeps more original data's pattern, and in the same scale as logged moving average, easier to compare RMSE.
    * Logged moving average format here is proved to be more forecastable and strict stationary through above analysis.
  * The results is showing `SARIMA` works better, and using logged moving averge is better.
  * Next, I want to see whether using the latest 2,3 weeks data for forecasting could work well. If so, then we'd better apply moving window as forecasting solution. Since using all the data for training may not be more reliable than using the latest data.
* [My Code - Forecast Experiments - Moving Window Solution][8]💖
  * Overall, moving window solution works well, even better than fixed window solution in most cases.
    * With fixed window, SARIMA appears to be better, with moving window solution, Holt Winters appears to be enough
  * 2 weeks training window is a bit better than 3 weeks.
  * Logged moving average is a bit better than logged time series.
* [My Code - Adjustable Forecasting - Moving Window Solution][9]💖
  * Params will be optimized after a new testing data had been put into the new training data. 
  * It works well for Sample 2 (the less forecastable data). For Sample 1, it can bring down the historical average RMSE.
  * Although here I'm using grid search, it was fast to run through all the moving windows. Which means, on production, we can use this method for just 1 moving window.
* [My Code - Prophet Forecasting - Fixed Window Solution][10]💖
  * Fixed window solution that I'm using all the historical data for training.
  * Prophet seems promising, it can handle NA automatically and smoothly. Its performace is also better than some moving window solutions for both samples.
  * Logged moving average time series still appears better than logged time series in general.
  * It seems that Prophet is building a function for the whole time series. So next I will try it with moving window solution to see how it goes.
* [My Code - Prophet Forecasting - Moving Window Solution][11]💖
  * Moving window solution. Same as previous experiments, divide the whole time series into several moving windows of train & test data, the latest test data will be added into the next traim data for next round of forecasting. The last RMSE is forecasting RMSE, while historical average RMSE is the average value from the list of historical moving windows.
  * Obviously, when using moving window & Prophet, the overall results are better than fixed window and other moving window solutions, for both samples, for both historical average RMSE and forecasting RMSE. Here, I even haven't used param tuning yet.
  * Comparing with moving window solution in Holt Winters, this method could take a bit longer time. However, in real life application, we don't calculate all the previous moving windows, they are majorly used for param tuning. So should be fine.
  
#### Summary
* After all these rounds of expderiments, <b>Prophet with Moving Window solution, using logged moving average time series</b> of this dataset is better than other solutions. Being better in almost all the aspects, for both representative samples, for both forecasting rmse and historical average rmse.

#### Forecast results shown to users
* [My Code - Forecasted Values][12]💖
  * We have to show user understandable forecating curves and values. To do this while keeping the accuracy is not that hard.
  * Still use Prophet & Moving Window & logged moving average time series
    * Since Prophet can handle missing values automatically, daily forecasted values can be shown to the user.
    * Then just get the exponential value from forecasted results will be what to show to the clients, the daily values.
* How does Prophet handle missing values
  * From [Prophet paper][13], it's not clearly mention how to handle missing data. But I think it's also because they build a function to fit the whole time series of both train and test data, therefore missing data is also covered.

### Products Recommendation Experiments
There are multiple recommendation methods in my mind now, so want to try them all to see which one works better.

#### Data Exploration
* [My Code - Merchant Products Observation][14]💖
  * The data should allow to try different types of recommendation.
  * I cannot use purchase frequency to caluclate product popularity since the daily, weekly frequencies are the same for all the products. Decide to use total purchase amount for product popularity.
  
#### Recommendation experiments
##### Popularity Recommendations
* [My Code - Popularity Recommendation & Forecasting][15]💖
  * Recommend the most popular & valuable products that a merchant is missing
  * Forecast sales in the next N days with selected recommended products
  * Here, I didn't recommend products based on the main categories the merchaant sells, assumed the merchant sells various categories of products. Better to divide merchants into groups, to see whether need to recommend based on categories for some merchants at the same time.
* [My Code - Group Merchants Exploration][16]💖
  * Was trying to see whether need to target merchants based on their main selling category. But the data here doesn't need to, since the smallest merchants also sells a wide variety of products, popularity recommendation won't add obvious daily increase in the following 1 week.
* [My Code - Recommendation & Forecast for small business][20]💙
  * All the merchants in the original dataset are large grocery stores, so I created a mockup small grocery store by removing those large/expensive items that most small grocery doesn't sell, and also reduced daily clients.
  * Now the daily forecasted profits increase is obvious but forecasting looks bad.... So better not to show the forecasted daily visualization for the increase, but to show the numbers of the forecasting (avg daily profits increase, and total increase).

* Summary
  * This recommendation method is easy, and since all the stores are grocery stores which sells more than thousands of products, the recommendation won't show obvious sales increase in the follwoing short term.
  * Better to show average daily increase & total increase for forecasted profits.
  
##### Freuqent Itemset Recommendations
* [My Code - Frequent Itemsets Recommendation][19]💙
  * The purpose here was to find the frequent itemsets to recommend merchants with the missing products.
  * But both FP-growth and PrefixSPAN only got (fresh fruits, fresh vegetables) as the frequent itemsets, with low support and low confidence. This finding is already common in grocery stores, and it's not very useful to recommend them to the merchants.
  * [GSP (Generalized Sequential Pattern) vs PrefixSPAN][17]
  * [FP-growth vs GSP][18]
    * FP-Growth is similar to Apriori, it mines the complete set of frequent itemsets without candidate generation. FP-growth compresses the database into a frequent-pattern tree, or FP-tree based on the frequency-descending list.
    * The GSP algorithm does the same work of Apriori algorithm, but it doesn't require finding all the frequent itemsets first.
    * "GSP is an iterative algorithm. It scans the database number of times depending on the length of the longest frequent sequences in database. The I/O cost is substantial (large) if database contains very long frequent sequences."
    * "PrefixSpan mines the complete set of patterns but greatly reduces the efforts of candidate sequence generation. A comprehensive performance study shows that PrefixSpan, in most cases, outperforms the apriori-based algorithm, GSP,, FreeSPAN, SPADE."
    
##### Similarity Recommendations
* In the code, the main part here is to try to use ray to do parallel processing,since the groupby of dataframes here can be slow.
* [My Code - Calculate Merchants Similarities][21]💖
  * The key points I'm using to calculate merchants similarity are:
    * Top selled products
    * Store size
    * Merchant Name
  * In real world, the geo distance can also be very helpful.
  * In the code, the main part here is to try to use ray to do parallel processing,since the groupby of dataframes here can be slow.
* [My Code - Similarity Recommendation][22]💖
  * Using Collaborative Filtering for recommendation.
    * Merchant similarity score as the weight.
    * Choose recent N weeks most sold products as the product candidate list, excluding the most sold products of the target merchant.
    * Using the product frequency by default
  * If we recommend the top 7 products as popularity_recommendation method, the daily increase in this method is still higher.
  * If we want the forecasting curve obvious, mainly need to increase the number of recommended products.

#### Summary
* Collaborative Filtering appear to be more effective in terms of daily sales increase.
* If we want the forecasting curve obvious, mainly need to increase the number of recommended products.


## Future Work
* Choose different forecasting method automatically for each merchant?
* How to adjust model params in moving window solution?
  * I tried grid search above. But we can further improve efficiency by narrow down the search space along the way. Such as using the frequency of best params.
* Federated Learning for general forecasting model
  * Each client has its local model, and there is a general model for all of them with only params exchanged for optimized results.
* Explore any advanced research algorithms in time series forecasting that can forecast with added products
  * One of the idea is time series regressor: https://otexts.com/fpp2/regression.html
    * If we want to forecast total sales, then the predictors used in the regressor can be selected product's sales/purchase amount/etc.?
* Using graph DB for real time recommendation.
  * After a user just bought certain items, based on geo and purchased products, recommend other items and the nearby store.
* Explore more advanced recommendation algorithms


[1]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/prototype.pdf
[2]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/data_preprocessing.ipynb
[3]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/purchase_times_series_preparation.ipynb
[4]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/seasonal_decomposing.ipynb
[5]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/stationary_analysis.ipynb
[6]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/forecastable_analysis.ipynb
[7]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/forecast_experiemnts.ipynb
[8]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/forecast_moving_window.ipynb
[9]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/adjustable_forecasting.ipynb
[10]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/prophet_forecast.ipynb
[11]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/prophet_forecast_moving_window.ipynb
[12]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/forecast_counts.ipynb
[13]:https://peerj.com/preprints/3190.pdf
[14]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/explore_merchant_products.ipynb
[15]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/recommendation_experiments/popularity_recommendation.ipynb
[16]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/recommendation_experiments/popularity_group_merchant.ipynb
[17]:https://www.ijedr.org/papers/IJEDR1403022.pdf
[18]:https://arxiv.org/ftp/arxiv/papers/1311/1311.0350.pdf
[19]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/recommendation_experiments/frequent_items_recommendations.ipynb
[20]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/recommendation_experiments/mockup_small_business.ipynb
[21]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/recommendation_experiments/merchant_similarity.ipynb
[22]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/recommendation_experiments/similarity_recommendations.ipynb
