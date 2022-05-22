# check-kucoin-balance-using-ccxt
simple code for check kucoin balance  using ccxt

import ccxt

exchange = ccxt.kucoin({
    'apiKey': '****apiKey****',
    'secret': ''****secret****',',
    'password': ''***password*****',',

})


print(exchange)

balance = exchange.fetch_balance()
print(balance)
