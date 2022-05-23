import ccxt

exchange = ccxt.kucoin({
    'apiKey': '********',
    'secret': ''********',',
    'password': ''********',',

})


print(exchange)

balance = exchange.fetch_balance()
print(balance)
