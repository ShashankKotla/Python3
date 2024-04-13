import requests

def fetch_randmo_user():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page="
    response = requests.get(url)
    main_data = response.json()

    if main_data['success']:
        user = main_data['data']
        data_one = user['data'][2]
        return data_one
    else:
        raise Exception("Failed to get data!")

def main():
    try:
        data_one = fetch_randmo_user()
        print(data_one)
    except Exception as e:
        print('error at main:',str(e))


if __name__ == '__main__':
    main()