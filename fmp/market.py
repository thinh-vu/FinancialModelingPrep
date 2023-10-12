from .config import *

# ECONOMIC DATA

def treasury_rate(from_date='20230-01-01', to_date='2023-10-10', api_key=TOKEN):
    """
    Return a dataframe with treasury rate
    Parameters:
        from_date: from date, format: yyyy-mm-dd
        to_date: to date, format: yyyy-mm-dd
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v4/treasury?from={from_date}&to={to_date}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def economic_indicator(name='GDP', api_key=TOKEN):
    """
    Return a dataframe with economic indicator
    Parameters:
        name: name of the economic indicator. Some of the economic indicators include GDP, Real GDP, CPI, Unemployment rate, and more
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v4/economic?name={name}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def economics_calendar(from_date='2023-01-01', to_date='2023-10-10', api_key=TOKEN):
    """
    Return a dataframe with economics calendar
    Parameters:
        from_date: from date, format: yyyy-mm-dd
        to_date: to date, format: yyyy-mm-dd
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/economic_calendar?from={from_date}&to={to_date}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

# FOREX

def forex_list(api_key=TOKEN):
    """
    Return a dataframe with forex currency pairs
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/symbol/available-forex-currency-pairs?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None

def forex_quote_list(api_key=TOKEN):
    """
    Return a dataframe with forex quote list
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/quotes/forex?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def forex_quote(symbol='EURUSD', api_key=TOKEN):
    """
    Return a dataframe with forex quote
    Parameters:
        symbol: symbol of the forex currency pair
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/quote/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data, index=[0])
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def forex_chart_data(symbol='EURUSD', from_date='2023-01-01', to_date='2023-10-10', resolution='4hour', api_key=TOKEN):
    """
    Return a dataframe with forex chart data
    Parameters:
        symbol: symbol of the forex currency pair
        from_date: from date, format: yyyy-mm-dd
        to_date: to date, format: yyyy-mm-dd
        resolution: resolution of the chart. Possible values: 1min, 5min, 15min, 30min, 1hour, 4hour
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/historical-chart/{resolution}/{symbol}?from={from_date}&to={to_date}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def forex_daily(symbol='EURUSD', api_key=TOKEN):
    """
    Return a dataframe with forex daily data
    Parameters:
        symbol: symbol of the forex currency pair
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/historical-price-full/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['historical'])
        df['symbol'] = data['symbol']
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

# CRYPTO

def crypto_list(api_key=TOKEN):
    """
    Return a dataframe with crypto list
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/symbol/available-cryptocurrencies?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None

def crypto_quote_list(api_key=TOKEN):
    """
    Return a dataframe with crypto quote list
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/quotes/crypto?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None

def crypto_quote(symbol='BTCUSD', api_key=TOKEN):
    """
    Return a dataframe with crypto quote
    Parameters:
        symbol: symbol of the crypto currency pair
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/quote/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None

def crypto_chart_data(symbol='BTCUSD', resolution='1min', from_date='2023-01-01', to_date='2023-10-10'):
    """
    Return a dataframe with crypto chart data
    Parameters:
        symbol: symbol of the crypto currency pair
        resolution: resolution of the chart. Possible values: 1min, 5min, 15min, 30min, 1hour, 4hour
        from_date: from date, format: YYYY-mm-dd
        to_date: to date, format: YYYY-mm-dd
    """
    url = f"{FMP_DOMAIN}/api/v3/historical-chart/{resolution}/{symbol}?from={from_date}&to={to_date}&apikey={token}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None

def crypto_daily(symbol='BTCUSD', api_key=TOKEN):
    """
    Return a dataframe with crypto daily data
    Parameters:
        symbol: symbol of the crypto currency pair
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/historical-price-full/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()['historical']
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
# COMMODITIES

def commodities_list(api_key=TOKEN):
    """
    Return a dataframe with commodities list
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/symbol/available-commodities?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def commodities_quote_list(api_key=TOKEN):
    """
    Return a dataframe with commodities quote list
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/quotes/commodity?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def commodities_quote(symbol='OUSX', api_key=TOKEN):
    """
    Return a dataframe with commodities quote
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/quote/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data, index=[0])
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def commodities_chart_data(symbol='OUSX', from_date='2023-09-01', to_date='2023-10-10', resolution='1min', api_key=TOKEN):
    """
    Return a dataframe with commodities chart data
    Parameters:
        symbol: symbol of the commodity
        from_date: from date, format: yyyy-mm-dd
        to_date: to date, format: yyyy-mm-dd
        resolution: resolution of the chart. Possible values: 1min, 5min, 15min, 30min, 1hour, 4hour
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/historical-chart/{resolution}/{symbol}?from={from_date}&to={to_date}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def commodities_daily(symbol='OUSX', api_key=TOKEN):
    """
    Return a dataframe with commodities daily data
    Parameters:
        symbol: symbol of the commodity
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v3/historical-price-full/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()['historical']
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
# MARKET DATA

def market_indices(api_key=TOKEN):
    """
    Return a dataframe with market indices
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v3/quotes/index?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def sector_pe(date='2023-10-11', exchange='NYSE', api_key=TOKEN):
    """
    Return a dataframe with sector PE ratio
    Parameters:
        date: date, format: YYYY-mm-dd
        exchange: exchange. Possible values: NYSE, NASDAQ, AMEX
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v4/sector_price_earning_ratio?date={date}&exchange={exchange}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def industry_pe(date='2023-10-11', exchange='NYSE', api_key=TOKEN):
    """
    Return a dataframe with industry PE ratio
    Parameters:
        date: date, format: YYYY-mm-dd
        exchange: exchange. Possible values: NYSE, NASDAQ, AMEX
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v4/industry_price_earning_ratio?date={date}&exchange={exchange}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def sector_performance(api_key=TOKEN):
    """
    Return a dataframe with sector performance
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v3/historical-sectors-performance?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def sector_historical(api_key=TOKEN):
    """
    Return a dataframe with sector historical performance
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v3/historical-sectors-performance?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None