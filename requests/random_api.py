import requests
from requests.exceptions import HTTPError



url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
random_data = requests.get(url)
data = random_data.json()
try:
    if random_data.status_code == 200 and data['data']:
        print("Successful")
        with open('output.txt', 'a') as file:
            user = data['data']
            name = user['name']['first']
            file.write(f'\n{name}')
            file.close()
        print(name)
        # file.close()
except HTTPError as e:
    print(f"Http Error occured: {e}")
except Exception as e2:
    print(f"Unexpected error : {e2}")
    






