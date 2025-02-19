import requests as request
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

response = request.get(url)

print(f'Status: {response.status_code}')

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.title.string)

book_titles_tag = soup.find_all('h3')
book_prices_tag = soup.find_all('p', class_='price_color')

book_titles = [title_tag.a['title'] for title_tag in book_titles_tag]
book_prices = [price_tag.string for price_tag in book_prices_tag]

for title, price in zip(book_titles, book_prices):
    print(f'book: {title} - {price}"/-"')
