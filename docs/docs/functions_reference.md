# Function References

Before we dig deeper, let's assign the FMP API key to a variable named `token`. This name will be referenced in the following examples.
Please refer to the [Pricing Page](https://intelligence.financialmodelingprep.com/pricing-plans?couponCode=thinhvu&utm_source=github&utm_medium=thinhvu_repos&utm_campaign=thinhvu) for more information about the different plans.


## Stock List
All of functions in this section are available for the Basic Plan (Free).

### Symbol List
```
symbol_list(api_key=TOKEN)
```

Output
```
>>> symbol_list(api_key=TOKEN)
          symbol                                               name  ...  exchangeShortName type
0         3SUL.L                WisdomTree Sugar 3x Daily Leveraged  ...                LSE  etf
1        TCLB.TO             TD Canadian Long Term Federal Bond ETF  ...                TSX  etf
2            IWX                  iShares Russell Top 200 Value ETF  ...               AMEX  etf
3         XCD.TO  iShares S&P Global Consumer Discretionary Inde...  ...                TSX  etf
4         CBH.TO  iShares 1-10 Year Laddered Corporate Bond Inde...  ...                TSX  etf
...          ...                                                ...  ...                ...  ...
11177     CYBP.L  Rize UCITS ICAV - Rize Cybersecurity And Data ...  ...                LSE  etf
11178       INTL                             Main International ETF  ...                ETF  etf
11179        JJC  iPath Series B Bloomberg Copper Subindex Total...  ...               AMEX  etf
11180        SLV                               iShares Silver Trust  ...               AMEX  etf
11181  102110.KS                          Mirae Asset TIGER 200 ETF  ...                KSC  etf
```

### Exchange Traded Fund Search
```
etf_search(api_key=TOKEN)
```

Output
```
>>> etf_search(TOKEN)
          symbol                                               name  ...  exchangeShortName type
0         3SUL.L                WisdomTree Sugar 3x Daily Leveraged  ...                LSE  etf
1        TCLB.TO             TD Canadian Long Term Federal Bond ETF  ...                TSX  etf
2            IWX                  iShares Russell Top 200 Value ETF  ...               AMEX  etf
3         XCD.TO  iShares S&P Global Consumer Discretionary Inde...  ...                TSX  etf
4         CBH.TO  iShares 1-10 Year Laddered Corporate Bond Inde...  ...                TSX  etf
...          ...                                                ...  ...                ...  ...
11177     CYBP.L  Rize UCITS ICAV - Rize Cybersecurity And Data ...  ...                LSE  etf
11178       INTL                             Main International ETF  ...                ETF  etf
11179        JJC  iPath Series B Bloomberg Copper Subindex Total...  ...               AMEX  etf
11180        SLV                               iShares Silver Trust  ...               AMEX  etf
11181  102110.KS                          Mirae Asset TIGER 200 ETF  ...                KSC  etf

[11182 rows x 6 columns]
```

### Statement Symbols List
```
statement_symbol_list(api_key=TOKEN)
```

Output

```
>>> statement_symbol_list(api_key=TOKEN)
          symbol
0      000001.SZ
1      000002.SZ
2      000004.SZ
3      000005.SZ
4      000006.SZ
...          ...
51695      ZYT.L
51696       ZYXI
51697    ZZ-B.ST
51698       ZZLL
51699     ZZZ.TO
```

### Tradable Search
```
tradable_search(api_key=TOKEN)
```

### Commitment of traders report
> The Commitments of Traders (COT report) is a weekly market report from the Commodity Futures Trading Commission (CFTC) enumerating the holdings of participants in various markets in the United States.

> The Commodity Futures Trading Commission (Commission or CFTC) publishes the Commitments of Traders (COT) reports to help the public understand market dynamics. Specifically, the COT reports provide a breakdown of each Tuesday’s open interest for futures and options on futures markets in which 20 or more traders hold positions equal to or above the reporting levels established by the CFTC.

> Generally, the data in the COT reports is from Tuesday and released Friday. The CFTC receives the data from the reporting firms on Wednesday morning and then corrects and verifies the data for release by Friday afternoon.

```
cot_report(api_key=TOKEN)
```

### CIK List
```
cik_list(api_key=TOKEN)
```

### Euronext Symbols
```
euronext_symbols(api_key=TOKEN)
```

### Symbol Changes
```
symbol_changes(api_key=TOKEN)
```

### Exchange Symbols
```
exchange_symbols(exchange='NASDAQ', api_key=TOKEN)
```

## Stock Fundamentals
### Financial Statements List

- Get the list of available symbols

```python
get_symbol_list(api_key)
```

### Company Financial Statements

The financial statements, including balance sheet, income statement, and cash flow statement available in annual and quarterly format sourced from SEC filings.

#### Income Statements
> An income statement shows a company's revenues, expenses and profitability over a period of time. It is also sometimes called a profit-and-loss (P&L) statement or an earnings statement.
- Get the Income Statement of a specific symbol

```python
get_financial_report(symbol='ZZ-B.ST', api_key=token, reportType='income-statement', period='year', limit=400)
```

- Get the Income Statement by CIK
```python
get_financial_report(symbol=None, cik='0001318605', api_key=token, reportType='income-statement', period='quarter', limit=400)
```

#### Balance Sheet Statements
> The balance sheet is a financial statement that displays a company’s total assets, liabilities, and shareholder equity over a specific timeframe (quarterly or yearly). Investors can use this statement to determine if the company can fund its operations, meet its debt obligations, and pay a dividend.

- Get the Balance Sheet Statement of a specific symbol

```python
get_financial_report(symbol='ZZ-B.ST', api_key=token, reportType='balance-sheet-statement', period='year', limit=400)
```

#### Cashflow Statements
> The cash flow statement is a financial statement that highlights how cash moves through the company, including both cash inflows and outflows. This statement shows the cash flows in 3 main categories “Operating Cash Flows”, “Investing Cash Flows”, and “Financing Cash Flows”, which help investors to understand if the company is making money or losing money by conducting business.

- Get the Cash Flow Statement of a specific symbol
```python
get_financial_report(symbol='ZZ-B.ST', api_key=token, reportType='cash-flow-statement', period='year', limit=400)

```

### Sales Revenue By Segments

> The Revenue Geographic Segmentation API provides information on the geographic segmentation of revenue for a specific product or segment.

- Yearly revenue breakdown

```python
get_revenue_breakdown(symbol='AAPL', api_key=token, period='year', structure='flat')
```

- Quarterly breakdown
```python
get_revenue_breakdown(symbol='AAPL', api_key=token, period='quarter', structure='flat')
```

## Statement Analysis
### Key Metrics
Provides investors with an extensive selection of the most important and most commonly used financial metrics. These metrics span from liquidity ratios, leverage ratios, efficiency ratios, profitability ratios, market ratios, and other financial ratios.

```
fundamental_metrics(symbol='AAPL', period='annual', api_key=TOKEN)
```

### Key Metrics TTM
Key Metrics such as Market capitalization, PE ratio, Price to Sales Ratio, POCF ratio, Graham Net-Net, The key metrics are calculated quarter by quarter, year by year.

```
fundamental_metrics_ttm(symbol='AAPL', api_key=TOKEN)
```

### Ratios
A set of financial ratios for companies used to analyze the company. The ratios are calculated using data from the financial statements.
```
fundamental_ratios_ttm(symbol='AAPL', api_key=TOKEN)
```

### Ratios TTM
Shows the Trailing Twelve Month (TTM) value of a variety of valuation ratios, financial ratios, liquidity ratios, leverage ratios, efficiency ratios, profitability ratios, and market ratios.
```
cashflow_growth(symbol='AAPL', period='annual', api_key=TOKEN)
```

### Cashflow Growth
The DCF value represents a stock intrinsic value calculated from its free cash flow analysis
```
cashflow_growth(symbol='AAPL', period='annual', api_key=TOKEN)
```

### Income Growth
Shows the percentage growth in each of the categories listed under a company’s income statement. Some of the most influential growth rates include; revenue, cost of revenue, gross profit, operating expense, EBITDA, net income, and EPS.

```
income_growth(symbol='AAPL', period='annual', api_key=TOKEN)
```


### Balance Sheet Growth
Shows the percentage growth in each of the categories listed under a company’s balance sheet. Some of the most influential growth rates from this category include; cash & cash equivalents, inventory, short-term debt, long-term debt, retained earnings, assets, liabilities, and shareholder equity.

```
balance_sheet_growth(symbol='AAPL', period='annual', api_key=TOKEN)
```

### Financial Growth
Financial Statement Growth of a company based on its financial statement, it compares previous financial statement to get growth of all its statement. The growth is calculated quarter by quarter, year by year.

```
financial_growth(symbol='AAPL', period='annual', api_key=TOKEN)
```

### Financial Score

```
financial_score(symbol='AAPL', api_key=TOKEN)
```

### Owner Earnings

```
owner_earning(symbol='AAPL', api_key=TOKEN)
```

### Enterprise Values
```
enterprise_value(symbol='AAPL', period='quarter', api_key=TOKEN)
```


## Stock Calendars

### Earnings
#### Earnings Calendar
Planned earnings report date, EPS and revenue estimates and actuals by company.

```
earning_calendar(from_date='2023-10-12', to_date='2023-07-12', api_key=TOKEN)
```

#### Earnings Historical
Allows investors to gather information on a company’s past quarterly earnings disclosures. The information in this section includes; EPS and Revenue estimates, EPS and Revenue reported figures, the date (and quarter) of the earnings, and the time in which the company’s earnings were reported.

```
earning_calendar_historical(symbol='AAPL', api_key=TOKEN)
```

#### Earnings Confirmed
Confirmed earnings within selected time frame that contains fields like date, time, exchange and more.

```
earning_confirm(from_date='2023-01-01', to_date='2023-10-10', api_key=TOKEN)
```

#### Earnings Surprises
> Historical EPS earnings, to show the expected earnings and the actual earnings, providing the earnings surprise.

```
earning_surprise(symbol='AAPL', api_key=TOKEN)
```

### Dividends Calendar

Dividends Calendar
> Calendar of dividends for a selected time period, including the Adjusted Dividend

```
dividend_calendar(from_date='2023-10-12', to_date='2023-07-12', api_key=TOKEN)
```

Dividends Historical
> Dividend history for any stock, ETF, mutual fund, and more, including dividend declaration date, dividend record date, and dividend payment date

```
dividend_historical(symbol='AAPL', api_key=TOKEN)
```

### Splits Calendar

Splits Calendar
> A calendar of companies that have announced their upcoming stock split(s). This calendar provides the announcement date, the split date, the numerator, and the denominator of the stock split.

```
split_calendar(from_date='2023-10-12', to_date='2023-07-12', api_key=TOKEN)
```

Splits Historical
> All historical stock splits for stocks with numerator and denominator fields. Stock splits affect both the price and the number of shares issued.

```
split_historical(symbol='AAPL', api_key=TOKEN)
```



### IPO Calendar


```
ipo_confirmed(api_key=TOKEN)
```

```
ipo_prospectus(api_key=TOKEN)
```

```
ipo_calendar(api_key=TOKEN)

```

## Company Information

### Company Profile
A summary of important company information, including price, beta, market capitalization,description, headquarters, and more

```
company_profile(symbol='AAPL', api_key=TOKEN)
```

### Excecutive Compensation

```
executive_compensation(symbol='AAPL', api_key=TOKEN)
```

### Compensation Benchmark
```
compensation_benchmark(year='2022', api_key=TOKEN)
```

### Company Notes
```
company_notes(symbol='AAPL', api_key=TOKEN)
```

### Employee Count
```
employee_count(symbol='AAPL', api_key=TOKEN)
```

### Screener (Stock)
The simplest way to get the list of stocks that meet your criteria. You can query all data without providing any query parameters, default limit is 1000 or add query parameters to filter the results.

```
stock_screener(api_key=TOKEN)
```

Here is an example of adding query parameters to filter the results, for example:

```
stock_screener(api_key=token, limit=2000, country='US', sector='Consumer Cyclical')

```

Please check all available query parameters below:

| Query Parameter        | Type    | Example                                                                                                                                                                 |
|------------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| marketCapMoreThan     | number  | 1000000000                                                                                                                                                             |
| marketCapLowerThan    | number  | 1000000000                                                                                                                                                             |
| priceMoreThan         | number  | 100                                                                                                                                                                    |
| priceLowerThan        | number  | 100                                                                                                                                                                    |
| betaMoreThan          | number  | 1                                                                                                                                                                      |
| betaLowerThan         | number  | 1                                                                                                                                                                      |
| volumeMoreThan        | number  | 10000                                                                                                                                                                  |
| volumeLowerThan       | number  | 10000                                                                                                                                                                  |
| dividendMoreThan      | number  | 1                                                                                                                                                                      |
| dividendLowerThan     | number  | 1                                                                                                                                                                      |
| isEtf                 | Boolean | true                                                                                                                                                                   |
| isActivelyTrading     | Boolean | true                                                                                                                                                                   |
| sector                | String  | Consumer Cyclical, Energy, Technology, Industrials, Financial Services, Basic Materials, Communication Services, Consumer Defensive, Healthcare, Real Estate, Utilities, Industrial Goods, Financial, Services, Conglomerates |
| Industry              | String  | Autos, Banks, Banks Diversified, Software, Banks Regional, Beverages Alcoholic, Beverages Brewers, Beverages Non-Alcoholic, ..                                       |
| Country               | String  | US, UK, MX, BR, RU, HK, CA, ..                                                                                                                                        |
| exchange              | String  | nyse, nasdaq, amex, euronext, tsx, etf, mutual_fund, ..                                                    |
| limit                 | number  | 10                                                                                                                                                                    |


### Stock Grade
```
stock_grade(symbol='AAPL', limit=500, api_key=TOKEN)
```

Output
```

```
### Executives
```
company_executives(symbol='AAPL', api_key=TOKEN)
```

### Company Core Information Summary
```
company_core_info(symbol='AAPL', api_key=TOKEN)
```

### Market Cap
```
market_cap(symbol='AAPL', api_key=TOKEN)
```

### History Market Cap
```
historical_market_cap(symbol='AAPL', limit=100, api_key=TOKEN)
```

### All Countries
```
available_countries(api_key=TOKEN)
```

### Company Rating
```
company_rating(symbol='AAPL', api_key=TOKEN)
```

### Historical Rating
```
historical_rating(symbol='AAPL', api_key=TOKEN)
```

### Analyst Estimates
```
analyst_estimate(symbol='AAPL', api_key=TOKEN)
```

Optional: You can spefify the period and limit of the analyst estimates as query parameters, for example:

```
analyst_estimate(symbol='AAPL', api_key=token, period='quarter')

```

### Analyst Recommendation
```
analyst_recommendation(symbol='AAPL', api_key=TOKEN)
```

### Company Outlook
```
company_outlook(symbol='AAPL', api_key=TOKEN)
```

### Stock Peers
```
stock_peer(symbol='AAPL', api_key=TOKEN)
```

### Market Open
```
is_market_open(api_key=TOKEN)
```

### Delisted Companies
```
delisted_company(api_key=TOKEN)
```

## Quote

### Full Quote
```
full_quote(symbol='AAPL', api_key=TOKEN)
```

### Quote Order
```
quote_order(symbol='AAPL', api_key=TOKEN)
```

### Simple Quote
```
simple_quote(symbol='AAPL', ap_key=TOKEN)
```

### OTC Quote
```
otc_quote(symbol='AAPL', api_key=TOKEN)
```

### Exchange Prices
```
exchange_price(exchange='NYSE', api_key=TOKEN)
```

### Stock Price Change
```
stock_price_changes(symbol='AAPL', api_key=TOKEN)
```

### Aftermarket Trade
```
after_market_trade(symbol='AAPL', api_key=TOKEN)
```

### Aftermarket Quote
```
after_market_quote(symbol='AAPL', api_key=TOKEN)
```

### Batch Quote
```
batch_quote(symbol='AAPL', api_key=TOKEN)
```

### Batch Trade
```
batch_trade(symbol='AAPL', api_key=TOKEN)
```

### Last Forex
```
last_forex(symbol='AAPL', api_key=TOKEN)
```

### Last Crypto
```
last_crypto(symbol='BTCUSD', api_key=TOKEN)
```

### Real-time Price
```
realtime_price(symbol='AAPL', api_key=TOKEN)
```

### All Live Prices (Short)
```
all_live_price(api_key=TOKEN)
```

### Live Full Price w/ Orders
```
full_realtime_price(symbol='AAPL', api_key=TOKEN)
```

### Forex Prices
```
fx_price(symbol='EURUSD', api_key=TOKEN)
```

### All Forex Prices
```
all_fx_price(api_key=TOKEN)
```

## Stock News

### General News

```python
get_news(api_key=token, type='general', page=0)
```

### Stock News
```python
get_news(api_key=token, type='stock', page=0)
```
### Forex News
```python
get_news(api_key=token, type='forex', page=0)
```

### Press Releases
```python
get_news(api_key=token, type='press-releases', page=0, ticker='AAPL')
```

### Crypto News
get_news(api_key=token, type='crypto', page=0)

## Insider Trading

### Insider Trades RSS
```python
get_insider_trade_rss_feed(api_key=token, page=0)
```

### Insider Trades Search

```python
get_insider_trade(symbol='AAPL', api_key=token, page=0)
```

- symbol: symbol of the company
- api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/
- page: page number of the insider trade

### Transaction Types

```
get_insider_trade_transaction_type(TOKEN)
```

### Insiders By Symbol

```
get_insider_roaster(symbol='AAPL', api_key=TOKEN)
```

### Insider Trade Statistics
> The return on investment (ROI) on US debt is known as Treasury rates. This is available on a daily basis and psance form 1-month to 30 year rates

```
get_insider_roaster_statistic('AAPL', api_key=TOKEN)
```

### CIK Mapper Name List
```
get_cik_mapper(token, page=0)
```

### CIK Mapper By Name
```
get_company_maker(name='AA', api_key=token, page=0)
```

### CIK Mapper Company
get_cik_mapper_company("AAPL", TOKEN)

## Econnomics Data

### Treasury Rates
The return on investment (ROI) on US debt is known as Treasury rates. This is available on a daily basis and psance form 1-month to 30 year rates

```
treasury_rate(from_date='2023-01-01', to_date='2023-10-10', api_key=TOKEN)
```

### Economic Indicator
Key economic indicators queried for a specified time range. Some of the economic indicators include GDP, Real GDP, CPI, Unemployment rate, and more

```
economic_indicator(name='GDP', api_key=TOKEN)
```

### Economics Calendar

```
economics_calendar(from_date='2023-01-01', to_date='2023-10-10', api_key=TOKEN)
```

## Market Overview
### Market Indexes

```
market_indices(api_key=TOKEN)
```

### Sector PE Ratio

```
sector_pe(date='2023-10-11', exchange='NYSE', api_key=TOKEN)
```

### Industry PE Ratio
```
industry_pe(date='2023-10-11', exchange='NYSE', api_key=TOKEN)
```

### Sector Performance

```
sector_performance(api_key=TOKEN)
```

### Sector Historical
```
sector_historical(api_key=TOKEN)
```

## Crypto 

### Crypto List

```
crypto_list(api_key=TOKEN)
```

### Full Quote List

```
crypto_quote_list(api_key=TOKEN)
```

### Full Quote

```
crypto_quote(symbol='BTCUSD', api_key=TOKEN)
```

### Chart Data

```
crypto_chart_data(symbol='BTCUSD', resolution='1min', from_date='2023-01-01', to_date='2023-10-10')
```

### Crypto Daily
```
crypto_daily(symbol='BTCUSD', api_key=TOKEN)
```



## Forex 
### Forex List

```
forex_list(api_key=TOKEN)
```

### Full Quote List
```
forex_quote_list(api_key=TOKEN)
```

### Full Quote

```
forex_quote(symbol='EURUSD', api_key=TOKEN)
```

### Chart Data

```
forex_chart(symbol='EURUSD', from_date='2023-01-01', to_date='2023-10-10', resolution='1min', api_key=TOKEN)
```

### Forex Daily

```
forex_daily(symbol='EURUSD', api_key=TOKEN)
```

## Commodities

### Commodities List

```
commodities_list(api_key=TOKEN)
```

### Full Quote List

```
commodities_quote_list(api_key=TOKEN)
```

### Full Quote

```
commodities_quote(symbol='OUSX', api_key=TOKEN)
```

### Chart Data

```
commodities_chart_data(symbol='DXUSD', from_date='2023-01-01', to_date='2023-10-10', resolution='1min', api_key=TOKEN)
```

### Commodities Daily
```
commodities_daily(symbol='OUSX', api_key=TOKEN)
```

