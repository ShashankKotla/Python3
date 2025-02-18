# import requests
# from requests.exceptions import HTTPError

# response = requests.get('https://api.github.com')
# print(response.status_code)

# if response.status_code == 200:
#     print("Successful!")
# elif response.status_code == 400:
#     print("Not Found!")

# if response: 
#request have default behaviour to validate (__bool__())
#     print("Success!")
# else:
#     raise Exception(f"Not-Success,{response.status_code}")

# URLS = ["https://api.github.com", "https://api.github.com/invalid"]

# for urls in URLS:
#     try:
#         response = requests.get(urls)
#         response.raise_for_status() 
#by adding this the HTTPError will be raised 
#     except HTTPError as http_err:
#         print(f'HTTP error {http_err}')
#     except Exception as err:
#         print(f'Other expection error {err}')
#     else:
#         print("Successful!")

# response = requests.get("https://api.github.com")
# print(response.content) 
#GET request often has some valuable information, known as a payload, in the message body. 
#To see the response’s content in bytes, you use .content
# print(type(response.content))

# response.encoding = 'utf-8' ## Optional: Requests infers this.
# print(response.text) #Now we get, serialized JSON content by setting up .encoding

# print(response.json()) #Dict data
# print(type(response.json())) #<class 'dict'>

# response_dict = response.json()
# print(response_dict["feeds_url"]) #.json() is a dictionary, so you can access values in the object by key

# information, like metadata about the response itself, then you’ll need to look at the response’s headers.
# print(response.headers) #Header Body
# print(response.headers['content-type']) #Note :  headers as case-insensitive

# response = requests.get("https://api.github.com/search/repositories", params={"q": "language:python", "sort": "stars", "order": "desc"})

# json_response = response.json()
# print(json_response)

# popular_repositories = json_response["items"]
# for repo in popular_repositories[:3]:
#     print(f"Name: {repo['name']}")
#     print(f"Description: {repo['description']}")
#     print(f"Stars: {repo['stargazers_count']}")
#     print()


