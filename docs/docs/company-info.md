---
sidebar_position: 2
---

# Company Information

> Below, you'll find a list of endpoints dedicated to company information. Each endpoint generates a Pandas DataFrame. The references for the output are displayed in the command line interface. For a more user-friendly view of the output, you can consult the Demo Notebook.

## Company Profile
A summary of important company information, including price, beta, market capitalization,description, headquarters, and more

```
company_profile(symbol='AAPL', api_key=TOKEN)
```

Output

```
>>> company_profile(symbol='AAPL', api_key=TOKEN)
  symbol   price      beta    volAvg         mktCap  ...  defaultImage  isEtf  isActivelyTrading  isAdr isFund
0   AAPL  180.71  1.286802  58009821  2825256201042  ...         False  False               True  False  False

[1 rows x 36 columns]
```

## Excecutive Compensation

```
executive_compensation(symbol='AAPL', api_key=TOKEN)
```

Output

```
>>> executive_compensation(symbol='AAPL', api_key=TOKEN).head()
          cik symbol companyName  ... all_other_compensation     total                                                url
0  0000320193   AAPL  Apple Inc.  ...                  17137  26251824  https://www.sec.gov/Archives/edgar/data/320193...
1  0000320193   AAPL  Apple Inc.  ...                  18337  27150352  https://www.sec.gov/Archives/edgar/data/320193...
2  0000320193   AAPL  Apple Inc.  ...                  37684  26272371  https://www.sec.gov/Archives/edgar/data/320193...
3  0000320193   AAPL  Apple Inc.  ...                  61191  27020811  https://www.sec.gov/Archives/edgar/data/320193...
4  0000320193   AAPL  Apple Inc.  ...                  19783  27151798  https://www.sec.gov/Archives/edgar/data/320193...

[5 rows x 15 columns]
```

## Compensation Benchmark
```
compensation_benchmark(year='2022', api_key=TOKEN)
```

Output

```
>>> compensation_benchmark(year='2022', api_key=TOKEN)
                                         industryTitle  year  averageCompensation
0                                 ADHESIVES & SEALANTS  2022         4.262500e+05
1     AGRICULTURAL PROD-LIVESTOCK & ANIMAL SPECIALTIES  2022         3.123146e+05
2                                 AIR COURIER SERVICES  2022         7.712610e+05
3                                             AIRCRAFT  2022         1.964232e+06
4                                     AIRCRAFT & PARTS  2022         5.297654e+05
..                                                 ...   ...                  ...
133    WHOLESALE-LUMBER & OTHER CONSTRUCTION MATERIALS  2022         5.684227e+05
134          WHOLESALE-MACHINERY, EQUIPMENT & SUPPLIES  2022         5.230000e+05
135  WHOLESALE-MEDICAL, DENTAL & HOSPITAL EQUIPMENT...  2022         5.640770e+05
136           WHOLESALE-MISCELLANEOUS NONDURABLE GOODS  2022         2.423333e+05
137         WOOD HOUSEHOLD FURNITURE, (NO UPHOLSTERED)  2022         4.471890e+05

[138 rows x 3 columns]
```

## Company Notes
```
company_notes(symbol='AAPL', api_key=TOKEN)
```

Output

```
>>> company_notes(symbol='AAPL', api_key=TOKEN)
          cik symbol                  title exchange
0  0000320193   AAPL  1.000% Notes due 2022   NASDAQ
1  0000320193   AAPL  1.375% Notes due 2024   NASDAQ
2  0000320193   AAPL  0.000% Notes due 2025   NASDAQ
3  0000320193   AAPL  0.875% Notes due 2025   NASDAQ
4  0000320193   AAPL  1.625% Notes due 2026   NASDAQ
5  0000320193   AAPL  2.000% Notes due 2027   NASDAQ
6  0000320193   AAPL  1.375% Notes due 2029   NASDAQ
7  0000320193   AAPL  3.050% Notes due 2029   NASDAQ
8  0000320193   AAPL  0.500% Notes due 2031   NASDAQ
9  0000320193   AAPL  3.600% Notes due 2042   NASDAQ
```

## Employee Count
```
employee_count(symbol='AAPL', api_key=TOKEN)
```

Output

```
>>> employee_count(symbol='AAPL', api_key=TOKEN).head()
  symbol         cik       acceptanceTime  ...  filingDate employeeCount                                             source
0   AAPL  0000320193  2022-10-27 18:01:14  ...  2022-10-28        164000  https://www.sec.gov/Archives/edgar/data/320193...
1   AAPL  0000320193  2021-10-28 18:04:28  ...  2021-10-29        154000  https://www.sec.gov/Archives/edgar/data/320193...
2   AAPL  0000320193  2020-10-29 18:06:25  ...  2020-10-30        147000  https://www.sec.gov/Archives/edgar/data/320193...
3   AAPL  0000320193  2019-10-30 18:12:36  ...  2019-10-31        137000  https://www.sec.gov/Archives/edgar/data/320193...
4   AAPL  0000320193  2018-11-05 08:01:40  ...  2018-11-05        132000  https://www.sec.gov/Archives/edgar/data/320193...

[5 rows x 9 columns]
```

## Screener (Stock)
The simplest way to get the list of stocks that meet your criteria. You can query all data without providing any query parameters, default limit is 1000 or add query parameters to filter the results.

```
stock_screener(api_key=TOKEN)
```

Output

```
>>> stock_screener(api_key=TOKEN)
     symbol                          companyName         marketCap  ... country  isEtf  isActivelyTrading
0    WEQ.TO                    WEQ Holdings Inc.  1534332425003000  ...    None  False              False
1      TAGS           Teucrium Agricultural Fund    41128965220000  ...      US   True               True
2      CORN                   Teucrium Corn Fund    30345394100000  ...      US   True               True
3      CANE                  Teucrium Sugar Fund    19628224280000  ...      US   True               True
4     KITTW              Nauticus Robotics, Inc.     9359396897200  ...      US  False               True
..      ...                                  ...               ...  ...     ...    ...                ...
995     UMC  United Microelectronics Corporation       18029326461  ...      TW  False               True
996     AIU                    Meta Data Limited       18008100864  ...      CN  False               True
997  GLE.PA     Société Générale Société anonyme       17855763569  ...      FR  False               True
998     HRL             Hormel Foods Corporation       17853535054  ...      US  False               True
999     EQT                      EQT Corporation       17852666023  ...      US  False               True

[1000 rows x 14 columns]
```


Here is an example of adding query parameters to filter the results, for example:

```
stock_screener(api_key=TOKEN, limit=2000, country='US', sector='Consumer Cyclical')

```

Output

```
>>> stock_screener(api_key=TOKEN, limit=2000, country='US', sector='Consumer Cyclical')
        symbol                    companyName      marketCap  ... country  isEtf  isActivelyTrading
0       M&M.NS    Mahindra & Mahindra Limited  1948176249434  ...      US  False               True
1      AMZN.NE               Amazon.com, Inc.  1850806590395  ...      US  False               True
2         AMZN               Amazon.com, Inc.  1365354533284  ...      US  False               True
3       AMZ.DE               Amazon.com, Inc.  1306233536717  ...      US  False               True
4        CCL.L     Carnival Corporation & plc  1209229705104  ...      US  False               True
..         ...                            ...            ...  ...     ...    ...                ...
896    1592.TW  Enterex International Limited              0  ...      US  False              False
897  138250.KS           NS Shopping Co., Ltd              0  ...      US  False              False
898     0RT7.L                   Tenneco Inc.              0  ...      US  False              False
899     0R16.L                Mcdonald's Corp              0  ...      US  False              False
900     0QZH.L                 Starbucks Corp              0  ...      US  False              False

[901 rows x 14 columns]
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


## Stock Grade
```
stock_grade(symbol='AAPL', limit=500, api_key=TOKEN)
```

Output
```
>>> stock_grade(symbol='AAPL', limit=500, api_key=TOKEN)
    symbol        date gradingCompany previousGrade      newGrade
0     AAPL  2023-08-17        Wedbush    Outperform    Outperform
1     AAPL  2023-08-16        Wedbush    Outperform    Outperform
2     AAPL  2023-08-04  Raymond James    Outperform    Outperform
3     AAPL  2023-08-04       Barclays  Equal-Weight  Equal Weight
4     AAPL  2023-08-04        Needham           Buy           Buy
..     ...         ...            ...           ...           ...
495   AAPL  2020-12-15        Cascend           Buy           Buy
496   AAPL  2020-12-14        Cascend           Buy           Buy
497   AAPL  2020-12-13    Wells Fargo    Overweight    Overweight
498   AAPL  2020-12-09        Wedbush    Outperform    Outperform
499   AAPL  2020-12-08        Wedbush    Outperform    Outperform

[500 rows x 5 columns]
```
## Executives
```
company_executives(symbol='AAPL', api_key=TOKEN)
```

Output

```
>>> company_executives(symbol='AAPL', api_key=TOKEN)
                                               title                     name  ...    titleSince symbol
0           Senior Vice President of People & Retail     Ms. Deirdre  O'Brien  ...  1.676249e+09   AAPL
1                 Chief Executive Officer & Director      Mr. Timothy D. Cook  ...           NaN   AAPL
2    Chief Financial Officer & Senior Vice President        Mr. Luca  Maestri  ...           NaN   AAPL
3                            Chief Operating Officer  Mr. Jeffrey E. Williams  ...           NaN   AAPL
4         Senior Vice President, Gen. Counsel & Sec.   Ms. Katherine L. Adams  ...           NaN   AAPL
5                    Senior Vice President of Retail     Ms. Deirdre  O'Brien  ...           NaN   AAPL
6          Senior Director of Corporation Accounting         Mr. Chris  Kondo  ...           NaN   AAPL
7                           Chief Technology Officer        Mr. James  Wilson  ...           NaN   AAPL
8                          Chief Information Officer          Ms. Mary  Demby  ...           NaN   AAPL
9   Senior Director of Investor Relations & Treasury        Ms. Nancy  Paxton  ...           NaN   AAPL
10      Senior Vice President of Worldwide Marketing        Mr. Greg  Joswiak  ...           NaN   AAPL

[11 rows x 8 columns]
```

## Company Core Information Summary
```
company_core_info(symbol='AAPL', api_key=TOKEN)
```

Output

```
>>> company_core_info(symbol='AAPL', api_key=TOKEN)
          cik symbol exchange  ...                         mailingAddress taxIdentificationNumber registrantName
0  0000320193   AAPL   NASDAQ  ...  ONE APPLE PARK WAY,CUPERTINO CA 95014              94-2404110     Apple Inc.

[1 rows x 13 columns]
```

## Market Cap
```
market_cap(symbol='AAPL', api_key=TOKEN)
```

Output

```
>>> market_cap(symbol='AAPL', api_key=TOKEN)
  symbol        date      marketCap
0   AAPL  2023-10-12  2825256201042
```

## History Market Cap
```
historical_market_cap(symbol='AAPL', limit=100, api_key=TOKEN)
```

Output

```
>>> historical_market_cap(symbol='AAPL', limit=100, api_key=TOKEN)
   symbol        date      marketCap
0    AAPL  2023-10-12  2836715825940
1    AAPL  2023-10-11  2822430997200
2    AAPL  2023-10-10  2800297361460
3    AAPL  2023-10-09  2809715929860
4    AAPL  2023-10-06  2786169508860
..    ...         ...            ...
95   AAPL  2023-05-26  2753832424020
96   AAPL  2023-05-25  2715530245860
97   AAPL  2023-05-24  2697477989760
98   AAPL  2023-05-23  2693082657840
99   AAPL  2023-05-22  2734524358800

[100 rows x 3 columns]
```

## All Countries
```
available_countries(api_key=TOKEN)
```

Output

```
>>> available_countries(api_key=TOKEN)
      0
0    FK
1    RU
2    DK
3    SN
4    SI
..   ..
109  IS
110  CR
111  MK
112  KH
113  GR

[114 rows x 1 columns]
```

## Company Rating
```
company_rating(symbol='AAPL', api_key=TOKEN)
```

Output

```
>>> company_rating(symbol='AAPL', api_key=TOKEN)
  symbol        date rating  ...  ratingDetailsPERecommendation ratingDetailsPBScore  ratingDetailsPBRecommendation
0   AAPL  2023-10-12      S  ...                     Strong Buy                    5                     Strong Buy

[1 rows x 17 columns]
```

## Historical Rating
```
historical_rating(symbol='AAPL', api_key=TOKEN)
```

Output

```
>>> historical_rating(symbol='AAPL', api_key=TOKEN)
     symbol        date rating  ...  ratingDetailsPERecommendation ratingDetailsPBScore  ratingDetailsPBRecommendation
0      AAPL  2023-10-12      S  ...                     Strong Buy                    5                     Strong Buy
1      AAPL  2023-10-11      S  ...                     Strong Buy                    5                     Strong Buy
2      AAPL  2023-10-10      S  ...                     Strong Buy                    5                     Strong Buy
3      AAPL  2023-10-09      S  ...                     Strong Buy                    5                     Strong Buy
4      AAPL  2023-10-06      S  ...                     Strong Buy                    5                     Strong Buy
...     ...         ...    ...  ...                            ...                  ...                            ...
5573   AAPL  2001-07-09     B+  ...                    Strong Sell                    3                        Neutral
5574   AAPL  2001-07-06     B+  ...                    Strong Sell                    3                        Neutral
5575   AAPL  2001-07-05     B+  ...                    Strong Sell                    3                        Neutral
5576   AAPL  2001-07-03     B+  ...                    Strong Sell                    3                        Neutral
5577   AAPL  2001-07-02     B+  ...                    Strong Sell                    3                        Neutral

[5578 rows x 17 columns]
```

## Analyst Estimates
```
analyst_estimate(symbol='AAPL', api_key=TOKEN)
```

Output

```
>>> analyst_estimate(symbol='AAPL', api_key=TOKEN).head()
  symbol        date  estimatedRevenueLow  ...  estimatedEpsLow  numberAnalystEstimatedRevenue  numberAnalystsEstimatedEps
0   AAPL  2024-12-30         2.936333e+11  ...         5.008968                             10
10
1   AAPL  2023-12-31         3.387104e+11  ...         4.810000                             12
12
2   AAPL  2022-12-31         3.079185e+11  ...         4.370000                             16
16
3   AAPL  2021-12-31         2.987380e+11  ...         3.400000                             14
14
4   AAPL  2020-12-31         1.999940e+11  ...         2.130000                             13
13

[5 rows x 22 columns]
```

Optional: You can spefify the period and limit of the analyst estimates as query parameters, for example:

```
analyst_estimate(symbol='AAPL', api_key=token, period='quarter')

```
Where period can be either 'quarter' or 'annual' and limit is the number of analyst estimates you want to get.

Output

```
>>> analyst_estimate(symbol='AAPL', api_key=TOKEN, period='quarter').head()
  symbol        date  estimatedRevenueLow  ...  estimatedEpsLow  numberAnalystEstimatedRevenue  numberAnalystsEstimatedEps
0   AAPL  2025-03-29         1.048101e+11  ...         1.476591                             18
18
1   AAPL  2024-12-30         4.885256e+10  ...         0.778242                             18
18
2   AAPL  2024-09-29         7.006572e+10  ...         1.209069                             14
14
3   AAPL  2024-06-29         5.875709e+10  ...         0.994242                             20
20
4   AAPL  2024-03-31         8.823863e+10  ...         1.300000                             20
20

[5 rows x 22 columns]
```

## Analyst Recommendation
```
analyst_recommendation(symbol='AAPL', api_key=TOKEN)
```

Output

```
>>> analyst_recommendation(symbol='AAPL', api_key=TOKEN).head()
  symbol        date  analystRatingsbuy  ...  analystRatingsSell  analystRatingsStrongSell  analystRatingsStrongBuy
0   AAPL  2023-08-01                 21  ...                   0                         0                       11
1   AAPL  2023-07-01                 21  ...                   1                         0                       11
2   AAPL  2023-06-01                 20  ...                   1                         0                       10
3   AAPL  2023-05-01                 24  ...                   1                         0                       10
4   AAPL  2023-04-01                 24  ...                   1                         0                       10

[5 rows x 7 columns]
```

## Company Outlook
```
company_outlook(symbol='AAPL', api_key=TOKEN)
```

Output

```
>>> company_outlook(symbol='AAPL', api_key=TOKEN)
                                              ratios  ... symbol
0  [{'dividendYielTTM': 0.005201704388246361, 'di...  ...   AAPL

[1 rows x 54 columns]
```

## Stock Peers
```
stock_peer(symbol='AAPL', api_key=TOKEN)
```

Output

```
>>> stock_peer(symbol='AAPL', api_key=TOKEN)
  symbol                                          peersList
0   AAPL  [LPL, SNEJF, PCRFY, SONO, VZIO, MICS, WLDSW, K...
```

## Market Open
```
is_market_open(api_key=TOKEN)
```

Output

```
>>> is_market_open(api_key=TOKEN)
         stockExchangeName  ... stockMarketHours.closingHour
0  New York Stock Exchange  ...                04:00 p.m. ET

[1 rows x 8 columns]
```

## Delisted Companies
```
delisted_company(api_key=TOKEN)
```

Output:

```
>>> delisted_company(api_key=TOKEN)
   symbol                                       companyName exchange     ipoDate delistedDate
0    ASPY                 ASYMshares ASYMmetric S&P 500 ETF     AMEX  2021-03-10   2023-10-12
1    ZSPY                ASYMmetric Smart Alpha S&P 500 ETF     AMEX  2023-02-01   2023-10-11
2   LFACW                   LF Capital Acquisition Corp. II   NASDAQ  2018-06-29   2023-10-11
3    JIDA  JPMorgan ActiveBuilders International Equity ETF     AMEX  2021-07-08   2023-10-10
4     JUN                                  Juniper II Corp.     NYSE  2021-12-23   2023-10-09
..    ...                                               ...      ...         ...          ...
95    LCI                             Lannett Company, Inc.     NYSE  1997-01-02   2023-06-16
96   MLAC       Malacca Straits Acquisition Company Limited   NASDAQ  2020-08-14   2023-06-16
97  HCNEW            JAWS Hurricane Acquisition Corporation   NASDAQ  2021-08-05   2023-06-16
98  HCNEU            JAWS Hurricane Acquisition Corporation   NASDAQ  2021-06-11   2023-06-16
99   FIHD          UBS AG FI Enhanced Global High Yield ETN     AMEX  2016-02-22   2023-06-15

[100 rows x 5 columns]
```
