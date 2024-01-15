from getData import *
from apiKeys import *

def initbuy():
    #gets list of avalable stocks using the api-key
    Stocks = getData(f'https://financialmodelingprep.com/api/v3/available-traded/list?apikey={data_api}')
    tradeable = {}

    #collects a list of all tradable stocks
    for stocks in Stocks:
        tradeable[stocks['symbol']] = 1

    #gets stock data feed-back
    Stocks = getData(f'https://financialmodelingprep.com/api/v4/stock-news-sentiments-rss-feed?page=0&apikey={data_api}')

    #Algorithm - if stock is tradable and has a good feed-back score, gets added into the list.
    buylist = {}
    for stocks in Stocks:
        if stocks['symbol'] in tradeable:
            if stocks['symbol'] in buylist:
                buylist[stocks['symbol']] += stocks['sentimentScore']
            else:
                buylist[stocks['symbol']] = stocks['sentimentScore']

    #removes stocks score less tan 0.5 out of the list
    for symbol in list(buylist.keys()):
        if buylist[symbol] < 0.5:
            buylist.pop(symbol)
    listString = ""

    #prints final list- tradable with good score.

    for symbol in buylist.keys():
        print(f'{symbol} : {buylist[symbol]}')
        if listString != "":
            listString +=','
        listString += symbol


    return buylist, listString
