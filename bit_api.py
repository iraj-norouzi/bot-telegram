


import requests
def bit_usd():
    url = 'https://www.yobit.net/api/2/btc_usd/ticker'
    response = requests.get(url)
    response = response.json()
    price = response['ticker']['last']
    price = str(price)+' USD'
    return price
