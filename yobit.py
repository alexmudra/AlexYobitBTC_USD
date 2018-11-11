import requests

#ф-ія для того щоб отримувати курс валюти btc до долара

def get_btc():
    url = "https://yobit.net/api/2/btc_usd/ticker"
    response_yobit = requests.get(url).json() #ми отримали дікшінарі з відповіддю із сайту курсу валют yobit
    #print(response_yobit)
    price = response_yobit['ticker']['last'] #вивели з дікшінарі значення останнього курсу валюти (виведе щось подібне до 6634)

    return str(price) + 'usd'

get_btc() #визвали функцію