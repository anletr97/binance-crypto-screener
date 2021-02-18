""" Screener utils """
import csv
import requests
from requests import RequestException

# END_POINT = 'https://api.binance.com'
# URL = 'https://api.binance.com/api/v3/ticker/price'
# """ START HERE """

SYMBOLS_FILE_NAME = 'symbols.csv'


# API get all exchange info but mostly is used to get all symbols in binance market
URL1 = 'https://api.binance.com/api/v3/exchangeInfo'

def crawl_symbols():
    """
        Crawling all symbols from binance market
        and write down to csv <br/>

    """
        # TODO: new feature will be added later
            # 1. A cron job will call this method
    try:
        print('Start crawling....')
        json_res = requests.get(URL1).json()
        header = ['symbols']
        # Set newline = '' to trim blank line
        with open (SYMBOLS_FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            print('Start writing file....')
            symbol_cnt = 0
            # Write data
            for element in json_res['symbols']:
                # Each symbols will be stored different array
                # example: ['ABC'] is known as a row in python
                symbols = []
                symbol = element['symbol']
                symbols.append(symbol)
                writer.writerow(symbols)
                symbol_cnt += 1
    except FileNotFoundError as ex:
        print(str(ex))
    except RequestException as req_excep:
        print(str(req_excep))
    else:
        print('\''+ SYMBOLS_FILE_NAME
                +'\' has been successfully created with {} symbols.'.format(symbol_cnt))

# TODO remove later
crawl_symbols()
