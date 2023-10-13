from .config import *

# STOCK LIST

def symbol_list(api_key=TOKEN):
    """
    Return a list of stock symbols as a pandas dataframe.
    Parameters:
    api_key (str): The api key for FMP
    """
    url = f"https://financialmodelingprep.com/api/v3/etf/list?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print('Error in getting the data')

def etf_search(api_key=TOKEN):
    """
    Return a list of ETF symbols as a pandas dataframe.
    Parameters:
    api_key (str): The api key for FMP
    """
    url = f"https://financialmodelingprep.com/api/v3/etf/list?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print('Error in getting the data')

def statement_symbol_list(api_key=TOKEN):
    """
    Return a list of statement symbols as a pandas dataframe.
    Parameters:
        api_key (str): The api key for FMP
    """
    url = f"https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        # rename the column 0 to symbol
        df = df.rename(columns={0: 'symbol'})
        return df
    else:
        print('Error in getting the data')

def tradable_search(api_key=TOKEN):
    """
    Return a list of tradable symbols as a pandas dataframe.
    Parameters:
        api_key (str): The api key for FMP
    """
    url = f"https://financialmodelingprep.com/api/v3/available-traded/list?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print('Error in getting the data')

def cot_report(api_key):
    """
    Return a list of tradable symbols as a pandas dataframe.
    Parameters:
        api_key (str): The api key for FMP
    """
    url = f"https://financialmodelingprep.com/api/v4/commitment_of_traders_report/list?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print('Error in getting the data')

def cik_list(api_key=TOKEN):
    """
    Return a list of CIK symbols as a pandas dataframe.
    Parameters:
        api_key (str): The api key for FMP
    """
    url = f"https://financialmodelingprep.com/api/v3/cik_list?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print('Error in getting the data')

def euronext_symbols(api_key):
    """
    Return a list of Euronext symbols as a pandas dataframe.
    Parameters:
        api_key (str): The api key for FMP
    """
    url = f"https://financialmodelingprep.com/api/v3/symbol/available-euronext?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print('Error in getting the data')

def symbol_changes(api_key):
    """
    Return a list of symbol changes as a pandas dataframe.
    Parameters:
        api_key (str): The api key for FMP
    """
    url = f"https://financialmodelingprep.com/api/v4/symbol_change?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print('Error in getting the data')

def exchange_symbols(exchange='NASDAQ', api_key=TOKEN):
    url = f"https://financialmodelingprep.com/api/v3/symbol/{exchange}?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print('Error in getting the data')


# COMPANY INFORMATION

def company_profile(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the company profile
    Parameters:
        symbol (required): symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
        """
    url = f"{FMP_DOMAIN}/api/v3/profile/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()[0]
        df = pd.DataFrame(data, index=[0])
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def executive_compensation(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the executive compensation
    Parameters:
        symbol (required): symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/        """
    url = f"{FMP_DOMAIN}/api/v4/governance/executive_compensation?symbol={symbol}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def compensation_benchmark(year='2022', api_key=TOKEN):
    """
    Return a dataframe with the compensation benchmark
    Parameters:
        year: year, format: YYYY
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/        """
    url = f"{FMP_DOMAIN}/api/v4/executive-compensation-benchmark?year={year}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def company_notes(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the company notes
    Parameters:
        symbol (required): symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/        """
    url = f"{FMP_DOMAIN}/api/v4/company-notes?symbol={symbol}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def employee_count(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the historical employee count
    Parameters:
        symbol (required): symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/        """
    url = f"{FMP_DOMAIN}/api/v4/historical/employee_count?symbol={symbol}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def stock_screener(api_key=TOKEN, **kwargs):
    """
    Return a dataframe with the stock screener data. Default limit is 10000. You can add more query parameters to the function, refer to the documentation for more details.
    Parameters:
        kwargs: query parameters, default param is api_key
        """
    url = f"{FMP_DOMAIN}/api/v3/stock-screener?apikey={api_key}"
    response = requests.request("GET", url, params=kwargs)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def stock_grade(symbol='AAPL', limit=500, api_key=TOKEN):
    """
    Return a dataframe with the stock grade data.
    Parameters:
        symbol (required): symbol of the company
        """
    url = f"{FMP_DOMAIN}/api/v3/grade/{symbol}?limit={limit}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def company_executives(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the company executives data.
    Parameters:
        symbol (required): symbol of the company
        """
    url = f"{FMP_DOMAIN}/api/v3/key-executives/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def company_core_info(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the company core information.
    Parameters:
        symbol (required): symbol of the company
        """
    url = f"{FMP_DOMAIN}/api/v4/company-core-information?symbol={symbol}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def market_cap(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the market cap information.
    Parameters:
        symbol (required): symbol of the company
        """
    url = f"{FMP_DOMAIN}/api/v3/market-capitalization/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def historical_market_cap(symbol='AAPL', limit=100, api_key=TOKEN):
    """
    Return a dataframe with the historical market cap information.
    Parameters:
        symbol (required): symbol of the company
        """
    url = f"{FMP_DOMAIN}/api/v3/historical-market-capitalization/{symbol}?limit={limit}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def available_countries(api_key=TOKEN):
    """
    Return a dataframe with the available countries.
    """
    url = f"{FMP_DOMAIN}/api/v3/get-all-countries?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def company_rating(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the company rating.
    Parameters:
        symbol (required): symbol of the company
        """
    url = f"{FMP_DOMAIN}/api/v3/rating/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def historical_rating(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the historical rating.
    Parameters:
        symbol (required): symbol of the company
        """
    url = f"{FMP_DOMAIN}/api/v3/historical-rating/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def analyst_estimate(symbol='AAPL', api_key=TOKEN, **kwargs):
    """
    Return a dataframe with the analyst estimate.
    Parameters:
        symbol (required): symbol of the company
        period (optional): period. Possible values: annual, quarter
        limit (optional): limit of the number of records
        """
    url = f"{FMP_DOMAIN}/api/v3/analyst-estimates/{symbol}?apikey={api_key}"
    response = requests.request("GET", url, params=kwargs)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def analyst_recommendation(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the analyst recommendation.
    Parameters:
        symbol (required): symbol of the company
        """
    url = f"{FMP_DOMAIN}/api/v3/analyst-stock-recommendations/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def company_outlook(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the company outlook.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v4/company-outlook?symbol={symbol}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def stock_peer(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the stock peers.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v4/stock_peers?symbol={symbol}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def is_market_open(api_key=TOKEN):
    """
    Return a dataframe with the market open data.
    """
    url = f"{FMP_DOMAIN}/api/v3/is-the-market-open?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def delisted_company(api_key=TOKEN):
    """
    Return a dataframe with the delisted company data.
    """
    url = f"{FMP_DOMAIN}/api/v3/delisted-companies?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def fundamental_metrics(symbol='AAPL', period='annual', api_key=TOKEN):
    """
    Return a dataframe with key metrics for statement analysis. These metrics span from liquidity ratios, leverage ratios, efficiency ratios, profitability ratios, market ratios, and other financial ratios.
    Parameters:
        symbol (required): symbol of the company
        period: period. Possible values: annual, quarter
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v3/key-metrics/{symbol}?period={period}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def fundamental_metrics_ttm(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with key metrics Trailing Twelve Month (TTM) such as Market capitalization, PE ratio, Price to Sales Ratio, POCF ratio, Graham Net-Net, The key metrics are calculated quarter by quarter, year by year.
    Parameters:
        symbol (required): symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v3/key-metrics-ttm/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def fundamental_ratios_ttm(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the Trailing Twelve Month (TTM) value of a variety of valuation ratios, financial ratios, liquidity ratios, leverage ratios, efficiency ratios, profitability ratios, and market ratios.
    Parameters:
        symbol (required): symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v3/ratios-ttm/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def cashflow_growth(symbol='AAPL', period='annual', api_key=TOKEN):
    """
    Return a dataframe with cashflow growth data. The DCF value represents a stock intrinsic value calculated from its free cash flow analysis
    Parameters:
        symbol (required): symbol of the company
        period: period. Possible values: annual, quarter
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v3/cash-flow-statement-growth/{symbol}?period={period}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def income_growth(symbol='AAPL', period='annual', api_key=TOKEN):
    """
    Return a dataframe with income growth data. The DCF value represents a stock intrinsic value calculated from its free cash flow analysis
    Parameters:
        symbol (required): symbol of the company
        period: period. Possible values: annual, quarter
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v3/income-statement-growth/{symbol}?period={period}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def balance_sheet_growth(symbol='AAPL', period='annual', api_key=TOKEN):
    """
    Return a dataframe with balance sheet growth data. This data shows the percentage growth in each of the categories listed under a company’s balance sheet. 
    Parameters:
        symbol (required): symbol of the company
        period: period. Possible values: annual, quarter
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v3/balance-sheet-statement-growth/{symbol}?period={period}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def financial_growth(symbol='AAPL', period='annual', api_key=TOKEN):
    """
    Return a dataframe with financial growth data. This data is based on its financial statement, it compares previous financial statement to get growth of all its statement. The growth is calculated quarter by quarter, year by year.
    Parameters:
        symbol (required): symbol of the company
        period: period. Possible values: annual, quarter
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v3/financial-growth/{symbol}?period={period}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def financial_score(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with financial score data. 
    Parameters:
        symbol (required): symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v4/score?symbol={symbol}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data, index=[0])
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def owner_earning(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with owner earning data. 
    Parameters:
        symbol (required): symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v4/owner_earnings?symbol={symbol}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def enterprise_value(symbol='AAPL', period='quarter', api_key=TOKEN):
    """
    Return a dataframe with enterprise value data. 
    Parameters:
        symbol (required): symbol of the company
        period: period. Possible values: annual, quarter, ttm
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
        """
    url = f"{FMP_DOMAIN}/api/v3/enterprise-values/{symbol}?period={period}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None


# STOCK FUNDAMENTALS

def get_symbol_list(api_key=TOKEN):
    """
    Return a list of symbols that have financial statements
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v3/financial-statement-symbol-lists?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json(), columns=['symbol'])
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def get_financial_report(symbol='AAPL', api_key=TOKEN, reportType='income-statement', period='quarter', cik=None, limit=400):
    """
    Return a dataframe with financial data for a symbol
    Parameters:
        symbol: symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/
        reportType: type of the report. Possible values: income-statement, balance-sheet-statement, cash-flow-statement
        period: period of the report. Possible values: year, quarter
        limit: number of records to return. Possible values: 1-400
    """
    # if cik != None, add cik to the url after reportType
    # if period == 'year', skip it in the url
    
    if cik != None:
        if period == 'year':
            url = f"{FMP_DOMAIN}/api/v3/{reportType}/{cik}?limit={limit}&apikey={api_key}"
        elif period == 'quarter':
            url = f"{FMP_DOMAIN}/api/v3/{reportType}/{cik}?period={period}&limit={limit}&apikey={api_key}"
    else:
        if period == 'year':
            url = f"{FMP_DOMAIN}/api/v3/{reportType}/{symbol}?limit={limit}&apikey={api_key}"
        elif period == 'quarter':
            url = f"{FMP_DOMAIN}/api/v3/{reportType}/{symbol}?period={period}&limit={limit}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def get_revenue_breakdown(symbol='AAPL', api_key=TOKEN, period='quarter', structure='flat'):
    """
    Return a dataframe with revenue breakdown for a symbol
    Parameters:
        symbol: symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/
        period: period of the report. Possible values: year, quarter
        structure: structure of the report. Possible values: flat, hierarchy
    """
    # if period == 'year', skip it in the url
    if period == 'year':
        url = f"{FMP_DOMAIN}/api/v4/revenue-product-segmentation?symbol={symbol}&structure={structure}&apikey={api_key}"
    elif period == 'quarter':
        url = f"{FMP_DOMAIN}/api/v4/revenue-product-segmentation?symbol={symbol}&period={period}&structure={structure}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        report_ls = []
        for period in response.json():
            # get key value of the dictionary structure
            for key, value in period.items():
                df = pd.DataFrame.from_dict(value, orient='index', columns=[key])
                report_ls.append(df)

        df = pd.concat(report_ls, axis=1)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    


