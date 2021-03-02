"""
    Constant
"""

# FILE CONSTANT
F_LAST_24H_PRICE = 'Last_24h_price'
F_SYMBOLS = 'symbols'
F_CSV = 'csv'

# PROCESS NAME CONSTANT
P_CRAWL_LAST_24H_PRICE = 'Crawling last 24h price'
P_CRAWL_EXCHANGE_INFO = 'Crawling exchange info'

# STATUS CODE
STATUS_OK = 200

# LOGGER CONSTANT
FORMAT_LOG = '%(asctime)s %(message)s'
FORMAT_DATE = '%Y/%m/%d %I:%M:%S %p'
FILE_NAME = "log.txt"
INFO = '[INFO ]'
ERROR = '[ERROR]'

# SYMBOLS
SYMBOLS_POSTFIX = 'USDT'
SYMBOLS = ['ADA', 'BNB', 'BTC', 'ETH']

def get_symbols():
    """
        Return list of symbol with postfix
    """
    symbol_list = []
    for symbol in SYMBOLS:
        symbol_list.append(symbol + SYMBOLS_POSTFIX)
    return symbol_list