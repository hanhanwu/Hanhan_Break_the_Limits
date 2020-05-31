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
* [My Code - Forecast Experiments - Fixed Window Solution][7]💖
  * The purpose in these experiments is to find whether there is an algorithm works better for all the samples here.
  * The training data is using all the historical data, instead of the latest historical data, this is why it's called "fixed window solution".
  * I was using the 2 representative samples, using their logged and logged moving average formats.
    * Because logged data still keeps more original data's pattern, and in the same scale as logged moving average, easier to compare RMSE.
    * Logged moving average format here is proved to be more forecastable and strict stationary through above analysis.
  * The results is showing `SARIMA` works better, and using logged moving averge is better.
  * Next, I want to see whether using the latest 2,3 weeks data for forecasting could work well. If so, then we'd better apply moving window as forecasting solution. Since using all the data for training may not be more reliable than using the latest data.

## Future Workd
* Choose different forecasting method automatically for each merchant?
* How to adjust forecasting model or model params when the latest time series ahs changed?


[1]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/prototype.pdf
[2]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/data_preprocessing.ipynb
[3]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/purchase_times_series_preparation.ipynb
[4]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/seasonal_decomposing.ipynb
[5]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/stationary_analysis.ipynb
[6]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/forecastable_analysis.ipynb
[7]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/forecast_experiemnts.ipynb
