import requests
import misc
import pprint
import json


token = misc.token

#getUpdates = "https://api.telegram.org/bot745109047:AAEu0bVlQSOanftv1yibr4MrRQhdDlzPx08/getupdates"
#print(token) #перевіряєм чи працює

# створили url
URL = 'https://api.telegram.org/bot' + token + '/'
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
    data = get_updates()

    chat_id = data['result'][-1]['message']['chat']['id'] #знайшли в словниках і лістах chat_id
    message_text = data['result'][-1]['message']['text']
    message = {'chat_id': chat_id,
               'message_text':message_text}
    print("Out chat id is: ", message)

    return message


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

    answer = get_message()
    # print(answer)
    chat_id = answer['chat_id']
    # print(chat_id)
    send_message(chat_id, "Що бажаєте? ")



#точка входа
if __name__ == '__main__':
    main()
