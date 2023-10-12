from .config import *

def full_quote(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the full quote data.
    Parameters:
        symbol (required): symbol of the company
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
    
def quote_order(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the quote order data.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v3/quote-order/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def simple_quote(symbol='AAPL', ap_key=TOKEN):
    """
    Return a dataframe with the simple quote data.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v3/quote-short/{symbol}?apikey={ap_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def otc_quote(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the OTC quote data.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v3/otc/real-time-price/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def exchange_price(exchange='NYSE', api_key=TOKEN):
    """
    Return a dataframe with the exchange price data.
    Parameters:
        exchange (required): exchange
    """
    url = f"{FMP_DOMAIN}/api/v3/quotes/{exchange}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def stock_price_changes(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the stock price changes data.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v3/stock-price-change/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['symbol'] = symbol
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def after_market_trade(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the after market trade data.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v4/pre-post-market-trade/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def after_market_quote(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the after market quote data.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v4/pre-post-market/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def batch_quote(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the batch after market quote data.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v4/batch-pre-post-market/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def batch_trade(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the batch after market trade data.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v4/batch-pre-post-market-trade/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def last_forex(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the last forex data.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v4/forex/last/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def last_crypto(symbol='BTCUSD', api_key=TOKEN):
    """
    Return a dataframe with the last crypto data.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v4/crypto/last/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def realtime_price(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the real-time price data.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v3/stock/real-time-price/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = json_normalize(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def all_live_price(api_key=TOKEN):
    """
    Return a dataframe with the all real-time price data.
    """
    url = f"{FMP_DOMAIN}/api/v3/stock/real-time-price?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()['stockList']
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def full_realtime_price(symbol='AAPL', api_key=TOKEN):
    """
    Return a dataframe with the full real-time price data.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v3/stock/full/real-time-price/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    

def fx_price(symbol='EURUSD', api_key=TOKEN):
    """
    Return a dataframe with the fx price data.
    Parameters:
        symbol (required): symbol of the company
    """
    url = f"{FMP_DOMAIN}/api/v3/fx/{symbol}?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None
    
def all_fx_price(api_key=TOKEN):
    """
    Return a dataframe with the all fx price data.
    """
    url = f"{FMP_DOMAIN}/api/v3/fx?apikey={api_key}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print(f"Error in getting the data. {response.text}")
        return None