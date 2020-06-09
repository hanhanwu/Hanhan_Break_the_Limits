# Bank Fantasy - Golden Bridge

<p align="center">
<img src="https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/imgs/golden_triangle.png" width="600" height="300" />
</p>

## Prototype
* [Click Me ❣][1]

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
  
#### Forecasting Experiments
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
  
#### Forecasting Experiemnts Summary
* After all these rounds of expderiments, <b>Prophet with Moving Window solution, using logged moving average time series</b> of this dataset is better than other solutions. Being better in almost all the aspects, for both representative samples, for both forecasting rmse and historical average rmse.


## Future Workd
* Choose different forecasting method automatically for each merchant?
* How to adjust model params in moving window solution?
  * I tried grid search above. But we can further improve efficiency by narrow down the search space along the way. Such as using the frequency of best params.
* Federated Learning for general forecasting model
  * Each client has its local model, and there is a general model for all of them with only params exchanged for optimized results.


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
