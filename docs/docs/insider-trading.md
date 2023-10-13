---
sidebar_position: 7
---

# Insider Trading

## Insider Trades RSS
```python
get_insider_trade_rss_feed(api_key=token, page=0)
```

## Insider Trades Search

```python
get_insider_trade(symbol='AAPL', api_key=token, page=0)
```

- symbol: symbol of the company
- api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/
- page: page number of the insider trade

## Transaction Types

```
get_insider_trade_transaction_type(TOKEN)
```

## Insiders By Symbol

```
get_insider_roaster(symbol='AAPL', api_key=TOKEN)
```

## Insider Trade Statistics
> The return on investment (ROI) on US debt is known as Treasury rates. This is available on a daily basis and psance form 1-month to 30 year rates

```
get_insider_roaster_statistic('AAPL', api_key=TOKEN)
```

## CIK Mapper Name List
```
get_cik_mapper(token, page=0)
```

## CIK Mapper By Name
```
get_company_maker(name='AA', api_key=token, page=0)
```

## CIK Mapper Company
```
get_cik_mapper_company("AAPL", TOKEN)
```
