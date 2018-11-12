import requests

#ф-ія для того щоб отримувати курс валюти btc до долара

def get_btc():
    url = "https://yobit.net/api/2/btc_usd/ticker"
    response = requests.get(url).json() #ми отримали дікшінарі з відповіддю із сайту курсу валют yobit
    #print(response_yobit)
    price = response['ticker']['last'] #вивели з дікшінарі значення останнього курсу валюти (виведе щось подібне до 6634)
    #print(str(price))
    return str(price) + ' usd'


#print(get_btc()) #визвали функцію