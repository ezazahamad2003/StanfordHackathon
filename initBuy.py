from getData import *
from apiKeys import *

def initbuy():
    Stocks = getData(f'https://financialmodelingprep.com/api/v3/available-traded/list?apikey={data_api}')
    tradeable = {}
    for stocks in Stocks:
        tradeable[stocks['symbol']] = 1
    Stocks = getData(f'https://financialmodelingprep.com/api/v4/stock-news-sentiments-rss-feed?page=0&apikey={data_api}')

    buylist = {}
    for stocks in Stocks:
        if stocks['symbol'] in tradeable:
            if stocks['symbol'] in buylist:
                buylist[stocks['symbol']] += stocks['sentimentScore']
            else:
                buylist[stocks['symbol']] = stocks['sentimentScore']

    for symbol in list(buylist.keys()):
        if buylist[symbol] < 0.5:
            buylist.pop(symbol)

    listString = ""
    for symbol in buylist.keys():
        print(f'{symbol} : {buylist[symbol]}')
        if listString != "":
            listString +=','
        listString += symbol


    return buylist, listString
