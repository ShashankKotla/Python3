import requests
from requests.exceptions import HTTPError


try:
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)
    data = response.json()
    print(response.url)
    if response.status_code == 200 and data['data']:
        print(f"Succesful {response.status_code}")
        try:
            with open('get_input.txt', 'a') as file:
                user =  data['data']
                print('user success')
                name = user['author']
                quote = user['content']
                file.write(f'Author: \n{name} \n say\'s :- " {quote}" ')
                print(name)
                print(quote)
        except KeyError as e:
            print('key error', e)
except HTTPError as e2:
    print(f"Http Errot: {e2}")
