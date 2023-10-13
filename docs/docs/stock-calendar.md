---
sidebar_position: 5
---

# Stock Calendars

## Earnings
### Earnings Calendar
Planned earnings report date, EPS and revenue estimates and actuals by company.

```
earning_calendar(from_date='2023-10-12', to_date='2023-07-12', api_key=TOKEN)
```

### Earnings Historical
Allows investors to gather information on a company’s past quarterly earnings disclosures. The information in this section includes; EPS and Revenue estimates, EPS and Revenue reported figures, the date (and quarter) of the earnings, and the time in which the company’s earnings were reported.

```
earning_calendar_historical(symbol='AAPL', api_key=TOKEN)
```

### Earnings Confirmed
Confirmed earnings within selected time frame that contains fields like date, time, exchange and more.

```
earning_confirm(from_date='2023-01-01', to_date='2023-10-10', api_key=TOKEN)
```

### Earnings Surprises
> Historical EPS earnings, to show the expected earnings and the actual earnings, providing the earnings surprise.

```
earning_surprise(symbol='AAPL', api_key=TOKEN)
```

## Dividends Calendar

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

## Splits Calendar

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



## IPO Calendar


```
ipo_confirmed(api_key=TOKEN)
```

