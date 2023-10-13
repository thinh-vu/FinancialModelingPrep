---
sidebar_position: 3
---

# Statement Analysis
## Key Metrics
Provides investors with an extensive selection of the most important and most commonly used financial metrics. These metrics span from liquidity ratios, leverage ratios, efficiency ratios, profitability ratios, market ratios, and other financial ratios.

```
fundamental_metrics(symbol='AAPL', period='annual', api_key=TOKEN)
```

- period: Possible values: annual, quarter

- Output:
```
>>> fundamental_metrics(symbol='AAPL', period='annual', api_key=TOKEN).head()
  symbol        date calendarYear period  ...  payablesTurnover  inventoryTurnover       roe  capexPerShare
0   AAPL  2022-09-24         2022     FY  ...          3.486641          45.197331  1.969589      -0.660337
1   AAPL  2021-09-25         2021     FY  ...          3.889140          32.367933  1.500713      -0.663722
2   AAPL  2020-09-26         2020     FY  ...          4.008866          41.753016  0.878664      -0.421217
3   AAPL  2019-09-28         2019     FY  ...          3.499048          39.401364  0.610645      -0.568178
4   AAPL  2018-09-29         2018     FY  ...          2.930074          41.394338  0.555601      -0.671644

[5 rows x 61 columns]
```


## Key Metrics TTM
Key Metrics such as Market capitalization, PE ratio, Price to Sales Ratio, POCF ratio, Graham Net-Net, The key metrics are calculated quarter by quarter, year by year.

```
fundamental_metrics_ttm(symbol='AAPL', api_key=TOKEN)
```

- Output:
```
>>> fundamental_metrics_ttm(symbol='AAPL', api_key=TOKEN)
   revenuePerShareTTM  netIncomePerShareTTM  ...  debtToMarketCapTTM  symbol
0           24.458048              6.036586  ...             0.03868    AAPL

[1 rows x 61 columns]
```

## Ratios
A set of financial ratios for companies used to analyze the company. The ratios are calculated using data from the financial statements.
```
fundamental_ratios_ttm(symbol='AAPL', api_key=TOKEN)
```

- Output:
```
>>> fundamental_ratios_ttm(symbol='AAPL', api_key=TOKEN)
   dividendYielTTM  dividendYielPercentageTTM  peRatioTTM  ...  priceFairValueTTM  dividendPerShareTTM  symbol
0         0.005202                    0.52017   29.935794  ...          47.063673                 0.94    AAPL

[1 rows x 58 columns]
```

## Ratios TTM
Shows the Trailing Twelve Month (TTM) value of a variety of valuation ratios, financial ratios, liquidity ratios, leverage ratios, efficiency ratios, profitability ratios, and market ratios.
```
fundamental_ratios_ttm(symbol='AAPL', api_key=TOKEN)
```

- Output:
```
>>> fundamental_ratios_ttm(symbol='AAPL', api_key=TOKEN)
   dividendYielTTM  dividendYielPercentageTTM  peRatioTTM  ...  priceFairValueTTM  dividendPerShareTTM  symbol
0         0.005202                    0.52017   29.935794  ...          47.063673                 0.94    AAPL

[1 rows x 58 columns]
```

## Cashflow Growth
The DCF value represents a stock intrinsic value calculated from its free cash flow analysis

```
cashflow_growth(symbol='AAPL', period='annual', api_key=TOKEN)
```

- period: Possible values: annual, quarter

- Output:
```
>>> cashflow_growth(symbol='AAPL', period='annual', api_key=TOKEN).head()
         date symbol calendarYear  ... growthOperatingCashFlow  growthCapitalExpenditure  growthFreeCashFlow
0  2022-09-24   AAPL         2022  ...                0.174100                  0.034010            0.198918
1  2021-09-25   AAPL         2021  ...                0.289610                 -0.516623            0.266994
2  2020-09-26   AAPL         2020  ...                0.162600                  0.303573            0.245670
3  2019-09-28   AAPL         2019  ...               -0.103869                  0.211673           -0.081487
4  2018-09-29   AAPL         2018  ...                0.217554                 -0.040485            0.262150

[5 rows x 34 columns]
```

## Income Growth
Shows the percentage growth in each of the categories listed under a company’s income statement. Some of the most influential growth rates include; revenue, cost of revenue, gross profit, operating expense, EBITDA, net income, and EPS.

```
income_growth(symbol='AAPL', period='annual', api_key=TOKEN)
```

- period: Possible values: annual, quarter

- Output:
```
>>> income_growth(symbol='AAPL', period='annual', api_key=TOKEN).head()
         date symbol calendarYear  ... growthEPSDiluted  growthWeightedAverageShsOut  growthWeightedAverageShsOutDil
0  2022-09-24   AAPL         2022  ...         0.089127                    -0.029058                       -0.031966
1  2021-09-25   AAPL         2021  ...         0.710366                    -0.037508                       -0.037842
2  2020-09-26   AAPL         2020  ...         0.104377                    -0.060592                       -0.057403
3  2019-09-28   AAPL         2019  ...        -0.003356                    -0.068117                       -0.070238
4  2018-09-29   AAPL         2018  ...         0.295652                    -0.050192                       -0.047905

[5 rows x 30 columns]
```

## Balance Sheet Growth
Shows the percentage growth in each of the categories listed under a company’s balance sheet. Some of the most influential growth rates from this category include; cash & cash equivalents, inventory, short-term debt, long-term debt, retained earnings, assets, liabilities, and shareholder equity.

```
balance_sheet_growth(symbol='AAPL', period='annual', api_key=TOKEN)
```

- period: Possible values: annual, quarter

- Output:
```
>>> balance_sheet_growth(symbol='AAPL', period='annual', api_key=TOKEN).head()
         date symbol calendarYear  ... growthTotalInvestments  growthTotalDebt  growthNetDebt
0  2022-09-24   AAPL         2022  ...              -0.065004        -0.037284       0.074004
1  2021-09-25   AAPL         2021  ...               0.011455         0.109244       0.206383
2  2020-09-26   AAPL         2020  ...              -0.020630         0.040621       0.257031
3  2019-09-28   AAPL         2019  ...              -0.256327        -0.056218      -0.331568
4  2018-09-29   AAPL         2018  ...              -0.150515        -0.010348      -0.071506

[5 rows x 43 columns]
```

## Financial Growth
Financial Statement Growth of a company based on its financial statement, it compares previous financial statement to get growth of all its statement. The growth is calculated quarter by quarter, year by year.

```
financial_growth(symbol='AAPL', period='annual', api_key=TOKEN)
```

- period: Possible values: annual, quarter

- Output:
```
>>> financial_growth(symbol='AAPL', period='annual', api_key=TOKEN).head()
  symbol        date calendarYear period  ...  bookValueperShareGrowth  debtGrowth  rdexpenseGrowth  sgaexpensesGrowth
0   AAPL  2022-09-24         2022     FY  ...                -0.172793   -0.037284         0.197910           0.142038
1   AAPL  2021-09-25         2021     FY  ...                 0.003208    0.109244         0.168622           0.103284
2   AAPL  2020-09-26         2020     FY  ...                -0.231352    0.040621         0.156317           0.091587
3   AAPL  2019-09-28         2019     FY  ...                -0.093747   -0.056218         0.139154           0.092188
4   AAPL  2018-09-29         2018     FY  ...                -0.158436   -0.010348         0.229255           0.094620

[5 rows x 38 columns]
```

## Financial Score

```
financial_score(symbol='AAPL', api_key=TOKEN)
```

- Output:
```
>>> financial_score(symbol='AAPL', api_key=TOKEN)
  symbol  altmanZScore  piotroskiScore  workingCapital  ...          ebit      marketCap  totalLiabilities       revenue
0   AAPL      8.218706               8     -2304000000  ...  109174000000  2747554229268      274764000000  383933000000

[1 rows x 10 columns]
```

## Owner Earnings

```
owner_earning(symbol='AAPL', api_key=TOKEN)
```

- Output:
```
>>> owner_earning(symbol='AAPL', api_key=TOKEN)
    symbol        date  averagePPE  maintenanceCapex  ownersEarnings   growthCapex  ownersEarningsPerShare
0     AAPL  2023-07-01    0.128560     -2.093000e+09    2.428700e+10  0.000000e+00                1.540000
1     AAPL  2023-04-01    0.128560     -2.916000e+09    2.564400e+10  0.000000e+00                1.620000
2     AAPL  2022-12-31    0.128560     -4.660051e+09    2.934495e+10  8.730510e+08                1.840000
3     AAPL  2022-09-24    0.128560     -2.416592e+09    2.171041e+10 -8.724082e+08                1.350000
4     AAPL  2022-06-25    0.128560     -2.102000e+09    2.079000e+10  0.000000e+00                1.280000
..     ...         ...         ...               ...             ...           ...                     ...
130   AAPL  1990-12-31    0.061937     -6.292125e+07    1.639788e+08 -1.127875e+07                0.012452
131   AAPL  1990-09-30    0.059261     -6.780000e+07    2.990000e+07  0.000000e+00                0.002271
132   AAPL  1990-06-30    0.059261     -4.389014e+07    2.579099e+08 -6.909859e+06                0.018453
133   AAPL  1990-03-31    0.059261     -4.280000e+07    2.605000e+08  0.000000e+00                0.018353
134   AAPL  1989-12-31    0.059261     -5.766723e+07    2.034328e+08 -5.232767e+06                0.013972

[135 rows x 7 columns]
```

## Enterprise Values
```
enterprise_value(symbol='AAPL', period='quarter', api_key=TOKEN)
```

- period: Possible values: annual, quarter

- Output:
```
>>> enterprise_value(symbol='AAPL', period='quarter', api_key=TOKEN)
    symbol        date  stockPrice  ...  minusCashAndCashEquivalents  addTotalDebt  enterpriseValue
0     AAPL  2023-07-01  193.970000  ...                 2.840800e+10  1.092800e+11     3.125738e+12
1     AAPL  2023-04-01  164.900000  ...                 2.468700e+10  1.096150e+11     2.688230e+12
2     AAPL  2022-12-31  129.930000  ...                 2.053500e+10  1.111100e+11     2.155516e+12
3     AAPL  2022-09-24  150.430000  ...                 2.364600e+10  1.200690e+11     2.507873e+12
4     AAPL  2022-06-25  141.660000  ...                 2.750200e+10  1.196910e+11     2.381832e+12
..     ...         ...         ...  ...                          ...           ...              ...
147   AAPL  1986-09-30    0.149550  ...                 5.762000e+08  0.000000e+00     1.556393e+09
148   AAPL  1986-06-30    0.160160  ...                          NaN           NaN              NaN
149   AAPL  1986-03-31    0.126120  ...                          NaN           NaN              NaN
150   AAPL  1985-12-31    0.098214  ...                          NaN           NaN              NaN
151   AAPL  1985-09-30    0.070313  ...                 3.370000e+08  0.000000e+00     6.359789e+08

[152 rows x 8 columns]
```


