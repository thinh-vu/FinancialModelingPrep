---
sidebar_position: 1
---

# Stock List
All of functions in this section are available for the Basic Plan (Free).

## Symbol List
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

## Exchange Traded Fund Search
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

## Statement Symbols List
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

## Tradable Search
```
tradable_search(api_key=TOKEN)
```

## Commitment of traders report
> The Commitments of Traders (COT report) is a weekly market report from the Commodity Futures Trading Commission (CFTC) enumerating the holdings of participants in various markets in the United States.

> The Commodity Futures Trading Commission (Commission or CFTC) publishes the Commitments of Traders (COT) reports to help the public understand market dynamics. Specifically, the COT reports provide a breakdown of each Tuesday’s open interest for futures and options on futures markets in which 20 or more traders hold positions equal to or above the reporting levels established by the CFTC.

> Generally, the data in the COT reports is from Tuesday and released Friday. The CFTC receives the data from the reporting firms on Wednesday morning and then corrects and verifies the data for release by Friday afternoon.

```
cot_report(api_key=TOKEN)
```

## CIK List
```
cik_list(api_key=TOKEN)
```

## Euronext Symbols
```
euronext_symbols(api_key=TOKEN)
```

## Symbol Changes
```
symbol_changes(api_key=TOKEN)
```

## Exchange Symbols
```
exchange_symbols(exchange='NASDAQ', api_key=TOKEN)
```
