""" Binance task """
import csv
import requests
import json
import pandas as pd
from requests import RequestException

import utils
import constant
from urls import *

# LIST OF SYMBOL
lst_of_symbol = constant.get_symbols()

def get_last_24_price(symbols):
    """ get last 24h price of symbol """
    process_name = 'Get last 24h prices'
    utils.log(process_name)
    prices = []
  
    # Export csv
    outCsv(prices)

def get_price_list(symbols):
    process_name = "Get price list"
    prices = []
    if symbols:
        for symbol in symbols:
            payload = {'symbol':symbol}
            res = requests.get(URL_LAST_24H_PRICE, params=payload)
            # If request doesn't response 200 raise exception
            if res.status_code != constant.STATUS_OK:
                res.raise_for_status()
            else:
                prices.append(res.json())
    else:
        utils.log(process_name, True, "there are no symbols to fetch.")

    return prices

def outCsv(prices):
    """
        Handle exporting CSV process
    """
    file_name = utils.get_filename(constant.F_LAST_24H_PRICE, 'csv', True)
    process_name = 'Export CSV'
    utils.log(process_name)

    record_cnt = 0
    if prices:
        keys = []
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            # Get key from first response and export as header
            for key in prices[0].keys():
                keys.append(key)
            writer.writerow(keys)
            # Get price info with key and export data
            if keys:
                for price in prices:
                    row = []
                    for key in keys:
                        row.append(price[key])
                    writer.writerow(row)
                    record_cnt += 1
        utils.log(process_name, True, 'exported successfully with {} rows'.format(record_cnt))
        return record_cnt
    else:
        # Khong ton tai list return
        utils.log(process_name, True, 'there are no record to be exported')

def test():
    get_last_24_price(lst_of_symbol)


test()