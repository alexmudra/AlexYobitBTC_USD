import requests
import misc
import pprint
import json

from yobit import get_btc
from time import sleep


token = misc.token

#getUpdates = "https://api.telegram.org/bot745109047:AAEu0bVlQSOanftv1yibr4MrRQhdDlzPx08/getupdates"
#print(token) #перевіряєм чи працює

# створили url
URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id #створили глобальну перемінну (хоча в такому випадку краще використовувати клас)
last_update_id = 0


#f'https://api.telegram.org/bot{token}/'
#745109047:AAEu0bVlQSOanftv1yibr4MrRQhdDlzPx08/sendmessage?chat_id=284158456&text=HI%20again

#ф-ія працює з апдейтами
def get_updates():
    url = URL + "getupdates"
    #print(url) буде такий вивід https://api.telegram.org/bot745109047:AAEu0bVlQSOanftv1yibr4MrRQhdDlzPx08/getupdates
    serverResponse = requests.get(url)
    # print(serverResponse) #відповідь від сервера буде <Response [200]>
    # print(serverResponse.content, '\n') #отримали відповідь від сервера з контентом(вертає бінарні дані)

#конвертуємо бінарні дані з респонза в json об'єкт та дікшінарі
    # print("Корвертували респонса сервера в json і дікшінарі і зникне проблема з кодування кирилиці: ", serverResponse.json())
    return serverResponse.json()

#ф-ія для отримання повідомлень із сервера
def get_message():
    #відповідати тільки на останні повідомлення
    # напишемо код щоб відповідати тільки на нові повідомлення  = отримувати update_id кожного обновлення з сайту yobit
    # записувати його в перемінну
    # порівнювати його з останнім оновленням

    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object["update_id"] #витягуєм з updates.json(дікшінарі) останній update_id

    global last_update_id #показали що ми працюємо з раніше об'явленою глобальною перемінною

    #умова для перевірки update_id до нового(з новими даними) існуючого останнього елементу списку result
    if last_update_id != current_update_id:
        last_update_id = current_update_id


        chat_id = last_object['message']['chat']['id'] #знайшли в словниках і лістах chat_id
        message_text = last_object['message']['text']
        message = {'chat_id': chat_id,
               'text':message_text}
        #print("Out chat id is: ", message_text)

        return message

    return None


#Робимо ф-ію відправки повідомлення

def send_message(chat_id, text = " Whait a second please..."):
    url= URL + 'sendmessage?chat_id={}&text={}'.format(chat_id,text)
    #print(url)

    requests.get(url)



def main():
    """isDictionary = get_updates()"""
#print(type(isDictionary)) #перевірили чи ф-ія get_updates() дійсно повертає дікшінарі(так, повертає <class 'dict'>))\n"

#робимо файл з json для простоти і наглядності"
#with open('updates.json', 'w') as file:\n"
#json.dump(isDictionary, file, indent=2, ensure_ascii=False))

#get_message() #для експерименту визиваємо цю ф-ію
#send_message(14) #для експерименту визиваємо цю функцію

"""
створимо цикл while щоб постійно не запускати ф-ію send_message
"""
while True:
    answer = get_message()

    if answer != None:
        chat_id = answer['chat_id']
        #send_message(chat_id, "Що бажаєте? ")
        text = answer['text']
        #print("Out variable text is:", text)

    #перевірим як працює умова зі словом kasha
    # if 'exellent' in text:
    #     send_message(chat_id, 'What?')

    #пропишем умову для ф-ії get_btc

        if text  == '/btc':
            send_message(chat_id, get_btc())
    else:
        continue

    sleep(3) #спамить кожні 3 секунди сайт телеграма



#точка входа
if __name__ == '__main__':
    main()
