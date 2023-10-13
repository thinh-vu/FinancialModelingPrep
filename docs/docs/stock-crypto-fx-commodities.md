---
sidebar_position: 10
---

# Stocks, Crypto, Forex, and Commodities
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

- Parameters:
    - `symbol`: symbol of the crypto currency pair
    - `from_date`: from date, format: yyyy-mm-dd
    - `to_date`: to date, format: yyyy-mm-dd
    - `resolution`: resolution of the chart. Possible values: 1min, 5min, 15min, 30min, 1hour, 4hour

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

- Parameters:
    - `symbol`: symbol of the forex currency pair
    - `from_date`: from date, format: yyyy-mm-dd
    - `to_date`: to date, format: yyyy-mm-dd
    - `resolution`: resolution of the chart. Possible values: 1min, 5min, 15min, 30min, 1hour, 4hour

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

- Parameters:
    - `symbol`: symbol of the commodity
    - `from_date`: from date, format: yyyy-mm-dd
    - `to_date`: to date, format: yyyy-mm-dd
    - `resolution`: resolution of the chart. Possible values: 1min, 5min, 15min, 30min, 1hour, 4hour

### Commodities Daily
```
commodities_daily(symbol='OUSX', api_key=TOKEN)
```
