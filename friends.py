

import requests
import json
from datetime import date


current_date = str(date.today())
current_yare = (current_date.split('-'))[0]


ACCESS_TOKEN = 'd4a9431cd4a9431cd4a9431cc6d7bdccb6dd4a9d4a9431cb024c9205f6e9436f6cffe1a'
def calc_age(uid):

    payload = {'v': 5.81, 'access_token': ACCESS_TOKEN, 'fields': 'bdate', 'user_id': uid}
    r = requests.get('https://api.vk.com/method/users.get', params=payload)
    uid = (r.json()['response'])[0]['id']

    payload = {'v': 5.81, 'access_token': ACCESS_TOKEN, 'fields': 'bdate', 'user_id': uid}
    r2 = requests.get('https://api.vk.com/method/friends.get', params=payload)
    return r2


if __name__ == '__main__':
    res = calc_age('reigning')
    ages = []
    for i in (res.json()['response']['items']):
        for h in i.items():
            if h[0] == 'bdate':
                t = h[1].split('.')
                if len(t)>2:
                    delta=int(current_yare)-int(t[-1])
                    ages.append(delta)
    age_count={}
    for age in ages:
        if age in age_count:
            age_count[age]+=1
        else:
            age_count[age]=1
    sorted_counter = sorted(age_count.items(), key=lambda x: (-x[1], x[0]))
    print(sorted_counter)




