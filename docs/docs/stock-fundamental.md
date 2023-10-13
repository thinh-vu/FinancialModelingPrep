---
sidebar_position: 4
---

# Stock Fundamentals
## Financial Statements List

- Get the list of available symbols

```python
get_symbol_list(api_key)
```

## Company Financial Statements

The financial statements, including balance sheet, income statement, and cash flow statement available in annual and quarterly format sourced from SEC filings.

### Income Statements
> An income statement shows a company's revenues, expenses and profitability over a period of time. It is also sometimes called a profit-and-loss (P&L) statement or an earnings statement.
- Get the Income Statement of a specific symbol

```python
get_financial_report(symbol='ZZ-B.ST', api_key=token, reportType='income-statement', period='year', limit=400)
```

- Get the Income Statement by CIK
```python
get_financial_report(symbol=None, cik='0001318605', api_key=token, reportType='income-statement', period='quarter', limit=400)
```

### Balance Sheet Statements
> The balance sheet is a financial statement that displays a company’s total assets, liabilities, and shareholder equity over a specific timeframe (quarterly or yearly). Investors can use this statement to determine if the company can fund its operations, meet its debt obligations, and pay a dividend.

- Get the Balance Sheet Statement of a specific symbol

```python
get_financial_report(symbol='ZZ-B.ST', api_key=token, reportType='balance-sheet-statement', period='year', limit=400)
```

### Cashflow Statements
> The cash flow statement is a financial statement that highlights how cash moves through the company, including both cash inflows and outflows. This statement shows the cash flows in 3 main categories “Operating Cash Flows”, “Investing Cash Flows”, and “Financing Cash Flows”, which help investors to understand if the company is making money or losing money by conducting business.

- Get the Cash Flow Statement of a specific symbol
```python
get_financial_report(symbol='ZZ-B.ST', api_key=token, reportType='cash-flow-statement', period='year', limit=400)

```

## Sales Revenue By Segments

> The Revenue Geographic Segmentation API provides information on the geographic segmentation of revenue for a specific product or segment.

- Yearly revenue breakdown

```python
get_revenue_breakdown(symbol='AAPL', api_key=token, period='year', structure='flat')
```

- Quarterly breakdown
```python
get_revenue_breakdown(symbol='AAPL', api_key=token, period='quarter', structure='flat')
```

