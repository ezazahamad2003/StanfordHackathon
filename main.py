from initBuy import *
from buyOrder import *

buymap, listString = initbuy()

for symbol in buymap:
    responseCode, responseData = buy_order(symbol, 1)
    