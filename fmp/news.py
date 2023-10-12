from .config import *

# NEWS

def get_news(api_key, type='general', page=0, ticker=None):
    """ 
    Return a dataframe with news
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/
        type: type of the news. Possible values: general, forex, crypto, stock, press-releases
        page: page number of the news
    """
    # if type == general, forex, crypto then use api v4 otherwise stock and press-releases use api v3
    if type in ['general', 'forex', 'crypto']:
        url = f"{FMP_DOMAIN}/api/v4/{type}_news?page={page}&apikey={api_key}"
    elif type  == 'stock':
        url = f"{FMP_DOMAIN}/api/v3/{type}_news?page={page}&apikey={api_key}"
    elif type == 'press-releases':
        url = f"{FMP_DOMAIN}/api/v3/press-releases/{ticker}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def get_insider_trade_rss_feed(api_key, page=0):
    """
    Return a dataframe with insider trade rss feed
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/
        page: page number of the insider trade rss feed
    """
    url = f"{FMP_DOMAIN}/api/v4/insider-trading-rss-feed?page={page}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def get_insider_trade(symbol, api_key, page=0):
    """
    Return a dataframe with insider trade
    Parameters:
        symbol: symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/
        page: page number of the insider trade
    """
    url = f"{FMP_DOMAIN}/api/v4/insider-trading?symbol={symbol}&page={page}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def get_insider_trade_transaction_type(api_key):
    """
    Return a dataframe with insider trade transaction type
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v4/insider-trading-transaction-type?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def get_insider_roaster(symbol, api_key):
    """
    Return a dataframe with insider roaster
    Parameters:
        symbol: symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v4/insider-roaster?symbol={symbol}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def get_insider_roaster_statistic(symbol, api_key):
    """
    Return a dataframe with insider roaster statistic
    Parameters:
        symbol: symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/
    """
    url = f"{FMP_DOMAIN}/api/v4/insider-roaster-statistic?symbol={symbol}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def get_cik_mapper(api_key, page=0):
    """
    Return a dataframe with cik mapper
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/
        page: page number of the cik mapper
    """
    url = f"{FMP_DOMAIN}/api/v4/mapper-cik-name?page={page}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def get_company_maker(name, api_key, page=0):
    """
    Return a dataframe with company maker
    Parameters:
        name: name of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/ 
        page: page number of the company maker
    """
    url = f"{FMP_DOMAIN}/api/v4/mapper-cik-name?name={name}&page={page}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def get_cik_mapper_company(symbol, api_key):
    """
    Return a dataframe with cik mapper company
    Parameters:
        symbol: symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://site.financialmodelingprep.com/developer/docs/ 
    """
    url = f"{FMP_DOMAIN}/api/v4/mapper-cik-company/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None


# EARNING

def earning_calendar(from_date='2023-10-12', to_date='2023-07-12', api_key=TOKEN):
    """
    Return a dataframe with earning data. This shows the planned earnings report date, EPS and revenue estimates and actuals by company.
    Parameters:
        from_date: from date, format: YYYY-mm-dd
        to_date: to date, format: YYYY-mm-dd
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
        """
    url = f"{FMP_DOMAIN}/api/v3/earning_calendar?from={from_date}&to={to_date}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def earning_calendar_historical(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with earning historical data. The information in this section includes; EPS and Revenue estimates, EPS and Revenue reported figures, the date (and quarter) of the earnings, and the time in which the company’s earnings were reported.
    Parameters:
        symbol (required): symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
        """
    url = f"{FMP_DOMAIN}/api/v3/historical/earning_calendar/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def earning_confirm(from_date='2023-01-01', to_date='2023-10-10', api_key=TOKEN):
    """
    Return a dataframe with earning confirmed data. This shows the confirmed earnings within selected time frame that contains fields like date, time, exchange and more.
    Parameters:
        from_date: from date, format: YYYY-mm-dd
        to_date: to date, format: YYYY-mm-dd
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
        """
    url = f"{FMP_DOMAIN}/api/v4/earning-calendar-confirmed?from={from_date}&to={to_date}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def earning_surprise(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with earning surprise data. This shows the earning surprise of the company. The earning surprise is the difference between the actual reported earnings and the expected earnings.
    Parameters:
        symbol (required): symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
        """
    url = f"{FMP_DOMAIN}/api/v3/earnings-surprises/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

# DIVIDEND

def dividend_calendar(from_date='2023-10-12', to_date='2023-07-12', api_key=TOKEN):
    """
    Return a dataframe with the calendar of dividends for a selected time period, including the Adjusted Dividend
    Parameters:
        from_date: from date, format: YYYY-mm-dd
        to_date: to date, format: YYYY-mm-dd
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
        """
    url = f"{FMP_DOMAIN}/api/v3/stock_dividend_calendar?from={from_date}&to={to_date}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def dividend_historical(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the historical dividends for a company
    Parameters:
        symbol (required): symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
        """
    url = f"{FMP_DOMAIN}/api/v3/historical-price-full/stock_dividend/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['historical'])
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

# SPLIT

def split_calendar(from_date='2023-10-12', to_date='2023-07-12', api_key=TOKEN):
    """
    Return a dataframe with the calendar of splits for a selected time period
    Parameters:
        from_date: from date, format: YYYY-mm-dd
        to_date: to date, format: YYYY-mm-dd
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
        """
    url = f"{FMP_DOMAIN}/api/v3/stock_split_calendar?from={from_date}&to={to_date}&apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
    
def split_historical(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the historical splits for a company
    Parameters:
        symbol (required): symbol of the company
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
        """
    url = f"{FMP_DOMAIN}/api/v3/historical-price-full/stock_split/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()['historical']
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None


# IPO Calendar
def ipo_confirmed(api_key=TOKEN):
    """
    Return a dataframe with the confirmed calendar of ipo for a selected time period
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
        """
    url = f"{FMP_DOMAIN}/api/v4/ipo-calendar-confirmed?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def ipo_prospectus(api_key=TOKEN):
    """
    Return a dataframe with the prospectus calendar
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
        """
    url = f"{FMP_DOMAIN}/api/v4/ipo-calendar-prospectus?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def ipo_calendar(api_key=TOKEN):
    """
    Return a dataframe with the IPO calendar by symbol
    Parameters:
        api_key: API key for the FMP API. Get it in the section Your Details from https://financialmodelingprep.com/developer/docs/
        """
    url = f"{FMP_DOMAIN}/api/v3/ipo_calendar?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

