import requests
import time
from InstagramAPI import InstagramAPI


url = "https://api.telegram.org/bot702425285:AAElSrsa99nOv_aG4ZLE7iJk-x7rh9KAvko/"
def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_update_before(data):
    results=data['result']
    id_length=len(results)-2
    return results[id_length]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def get_name(update):
    name_id = update['message']['chat']['first_name']
    return name_id

def get_chat(update):
    chat_msg= update['message']['text']
    return chat_msg

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
chat_id = get_chat_id(last_update(get_updates_json(url)))
name_id = get_name(last_update(get_updates_json(url)))
chat_msg= get_chat(last_update(get_updates_json(url)))

#send_mess(chat_id, chat_msg)
#'Hola, ' + name_id + '. Esto es un bot.'

#def main():

    
    #update_id_before=get_update_id(get_updates_json(url))['update_id']
    # print(update_id)
    # print(update_id_before)
    #chat_msg = get_chat(last_update(get_updates_json(url)))
    while True:
        update_id = last_update(get_updates_json(url))['update_id']
        chat_msg = get_chat(last_update(get_updates_json(url)))
       # print(chat_msg)
        chat_msg_before = get_chat(get_update_before(get_updates_json(url)))
       # print(chat_msg)
        if update_id == last_update(get_updates_json(url))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(url))), 'Escriba /comando')
           if chat_msg=='/comando':
               send_mess(get_chat_id(last_update(get_updates_json(url))), 'Escriba el usuario')

           else:
                if chat_msg_before=='/comando':

                    username_ig=chat_msg

                    usr = 'bismabakery'
                    pwd = 'amorodio_19'

                    InstagramAPI = InstagramAPI(usr, pwd)
                    InstagramAPI.login()

                    InstagramAPI.getProfileData()
                    # user_id=InstagramAPI.LastJson['user']['pk']

                    user_name = username_ig

                    InstagramAPI.searchUsername(user_name)
                    user_id = InstagramAPI.LastJson["user"]["pk"]

                    # user_id='814703627'
                    # print(user_id)

                    InstagramAPI.getUserFollowings(user_id)
                    # print len(InstagramAPI.LastJson['users'])
                    following_list = InstagramAPI.LastJson['users']

                    followers = []
                    next_max_id = True
                    while next_max_id:
                        # print next_max_id
                        # first iteration hack
                        if next_max_id == True: next_max_id = ''
                        _ = InstagramAPI.getUserFollowers(user_id, maxid=next_max_id)
                        followers.extend(InstagramAPI.LastJson.get('users', []))
                        next_max_id = InstagramAPI.LastJson.get('next_max_id', '')
                        time.sleep(1)

                    followers_list = followers

                    user_list = map(lambda x: x['username'], followers_list)
                    followers_set = set(user_list)
                    # print 'Seguidores: ', len(followers_set)
                    # print (followers_set)
                    send_mess(get_chat_id(last_update(get_updates_json(url))), len(followers_set))
                    user_list = map(lambda x: x['username'], following_list)
                    following_set = set(user_list)
                    #print 'Siguiendo: ', len(following_set)
                    send_mess(get_chat_id(last_update(get_updates_json(url))), len(following_set))
                    # print(followers_set-following_set)
                    # print(user_id)

               #send_mess(get_chat_id(last_update(get_updates_json(url))), 'Escriba /comando')

           update_id += 1

    #sleep(1)

#if __name__ == '__main__':
 #   main()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
# import InstagramAPI
# from InstagramAPI import InstagramAPI


# # ##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# def igapp():
#     usr='bismabakery'
#     pwd='amorodio_19'
#
#     InstagramAPI = InstagramAPI(usr, pwd)
#     InstagramAPI.login()
#
#     InstagramAPI.getProfileData()
#     #user_id=InstagramAPI.LastJson['user']['pk']
#
#     user_name = username_ig
#
#     InstagramAPI.searchUsername(user_name)
#     user_id = InstagramAPI.LastJson["user"]["pk"]
#
#     #user_id='814703627'
#     #print(user_id)
#
#     InstagramAPI.getUserFollowings(user_id)
#     #print len(InstagramAPI.LastJson['users'])
#     following_list=InstagramAPI.LastJson['users']
#
#     followers = []
#     next_max_id = True
#     while next_max_id:
#         #print next_max_id
#         # first iteration hack
#         if next_max_id == True: next_max_id = ''
#         _ = InstagramAPI.getUserFollowers(user_id, maxid=next_max_id)
#         followers.extend(InstagramAPI.LastJson.get('users', []))
#         next_max_id = InstagramAPI.LastJson.get('next_max_id', '')
#         time.sleep(1)
#
#     followers_list = followers
#
#     user_list = map(lambda x: x['username'] , followers_list)
#     followers_set= set(user_list)
#    # print 'Seguidores: ', len(followers_set)
#     #print (followers_set)
#
#     user_list = map(lambda x: x['username'] , following_list)
#     following_set= set(user_list)
#     print 'Siguiendo: ', len(following_set)
#     #print(followers_set-following_set)
#     #print(user_id)
# #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
#
