""" List of url """
URL_EXCHANGE_INFO = 'https://api.binance.com/api/v3/exchangeInfo'
URL_LAST_24H_PRICE = 'https://api.binance.com/api/v3/ticker/24hr'
URL_KLINE = 'https://api.binance.com/api/v3/klines'

def get_kline_url(symbol, interval):
    """
        Get KLINE URL with symbol and interval
    """
    return URL_KLINE + '?symbol={}'.format(symbol)+'&interval={}'.format(interval)