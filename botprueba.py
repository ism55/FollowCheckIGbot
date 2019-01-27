url = "https://api.telegram.org/bot702425285:AAElSrsa99nOv_aG4ZLE7iJk-x7rh9KAvko/"
def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def get_name(update):
    name_id = update['message']['chat']['first_name']
    return name_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
chat_id = get_chat_id(last_update(get_updates_json(url)))
name_id = get_name(last_update(get_updates_json(url)))
send_mess(chat_id, 'Hola, ' + name_id + '. Esto es un bot.')
