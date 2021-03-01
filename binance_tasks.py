""" Screener utils """
import csv
import requests
import json
import pandas as pd
from requests import RequestException

import utils
import constant
from urls import *

# """ START HERE """

# API get all exchange info but mostly is used to get all symbols in binance market


def crawl_symbols():
    """
        Crawling all symbols from binance market
        and write down to csv
    """
    # TODO: new feature will be added later
    # 1. A cron job will call this method
    try:
        res = requests.get(URL_EXCHANGE_INFO).json()
        header = ['symbols']
        file_name = utils.get_filename(constant.F_SYMBOLS, constant.F_CSV)
        # Set newline = '' to trim blank line
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            symbol_cnt = 0
            # Write data
            for element in res['symbols']:
                # Each symbols will be stored different array
                # example: ['ABC'] is known as a row in python
                symbols = []
                symbol = element['symbol']
                symbols.append(symbol)
                writer.writerow(symbols)
                symbol_cnt += 1
    except RequestException as req_excep:
        print(str(req_excep))
    except IOError as io_excep:
        print(str(io_excep))
    else:
        print('\'' + file_name
              + '\' has been successfully created with {} symbols.'.format(symbol_cnt))

def crawl_24h_price():
    """
        Crawling last 24h price
    """
    fields = []
    try:
        utils.log(constant.P_CRAWL_LAST_24H_PRICE)
        # crawling request
        res = requests.get(URL_LAST_24H_PRICE)
        files = []
        if res.status_code == constant.STATUS_OK:
            file_name = utils.get_filename(
                constant.F_LAST_24H_PRICE, constant.F_CSV, True)
            symbol_cnt = 0
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                # Get keys to generate header
                for key in res.json()[0].keys():
                    fields.append(key)
                # write header
                writer.writerow(fields)
                # data
                for el in res.json():
                    row = []
                    for field in fields:
                        row.append(el[field])
                    writer.writerow(row)
                    symbol_cnt += 1
                    files.append(file)
            msg = '\'' + file_name + \
                    '\' has been successfully created for {} symbols.'.format(
                    symbol_cnt)
            utils.log(constant.P_CRAWL_LAST_24H_PRICE, True, msg)
            return files
        else:
            raise res.raise_for_status()
    except RequestException as req_excep:
        utils.error_log(constant.P_CRAWL_LAST_24H_PRICE, str(req_excep))

def craw_24h_json():
    """
        Crawling last 24h price
    """
    # fields = ['symbol','openTime','closeTime','openPrice','lowPrice','highPrice','lastPrice','prevClosePrice']
    # fields_1 = []
    files = []
    try:
        utils.log(constant.P_CRAWL_LAST_24H_PRICE)
        # crawling request
        res = requests.get(URL_LAST_24H_PRICE)
        if res.status_code == constant.STATUS_OK:
            res = res.json()
            # Edit file name
            file_name = utils.get_filename(
                constant.F_LAST_24H_PRICE, 'json', True)
            symbol_cnt = 0
            with open(file_name, 'w') as file:
                json.dump(res, file)
                files.append(file)
            return files
        else:
            raise res.raise_for_status()
    except RequestException as req_excep:
        utils.error_log(constant.P_CRAWL_LAST_24H_PRICE, str(req_excep))
    else:
        msg = '\'' + file_name + \
            '\' has been successfully created for {} symbols.'.format(
                symbol_cnt)
        utils.log(constant.P_CRAWL_LAST_24H_PRICE, True, msg)

def crawl_kline_data():
    """
        Crawl kline data
    """
    # 1. read symbols csv
    df = pd.read_csv('symbols.csv')
    # file name
    file_name = utils.get_filename('KLINES', constant.F_CSV, True)
    lst_symbol = df['symbols'].values.tolist()

    start = 0
    end = 500
    files = []
    fields = ['symbol','openTime','openPrice','highPrice','lowPrice', 'closePrice', 'volumne', 'closeTime', 'quoteAssetVolumne', 
                'numberOfTrades', 'takerBuyBaseAssetVol', 'takerBuyQuoteAssetVol','ignore']
    while start < len(lst_symbol):
        symbols = lst_symbol[start:end]
        # load symbols to url request
        for symbol in symbols:
            payload = {
                'symbol': symbol,
                'interval': '1h' # could set to m, h, ms
            }
            res = requests.get(URL_KLINE, params=payload)

            # if request return 200
            if (res.status_code == constant.STATUS_OK):
                with open(file_name, 'w', newline='') as file:
                    writer = csv.writer(file)
                    # write header
                    header = []
                    for field in fields:
                        header.append(field)
                    writer.writerow(fields)
                    for element in res['symbols']:
                        # Each symbols will be stored different array
                        # example: ['ABC'] is known as a row in python
                        symbols = []
                        symbol = element['symbol']
                        symbols.append(symbol)
                        writer.writerow(symbols)
                        symbol_cnt += 1
                    res = res.json()
                    for each in res:
                        print(each)
            else:
                raise res.raise_for_status()

    print(res)

# TODO remove later
# crawl_symbols()
# crawl_24h_price()
# craw_24h_json()
crawl_kline_data()
