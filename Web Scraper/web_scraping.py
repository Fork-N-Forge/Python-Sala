import requests
from bs4 import BeautifulSoup
import csv


url = 'https://example.com/quotes'


response = requests.get(url)


if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

   
    quotes = soup.find_all('div', class_='quote')

    data = []

    for quote in quotes:
        quote_text = quote.find('p', class_='quote-text').text
        author = quote.find('p', class_='author').text
        data.append({'quote': quote_text, 'author': author})

    csv_filename = 'quotes.csv'

 
    with open(csv_filename, 'w', newline='') as csv_file:
        fieldnames = ['quote', 'author']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f'Data scraped and saved to {csv_filename}')
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
