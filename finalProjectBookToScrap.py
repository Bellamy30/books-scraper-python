import requests
from bs4 import BeautifulSoup
import csv
import time
import logging

logging.basicConfig(
    filename='scraping.log', # Log file name
    level=logging.INFO,     # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'   # Log message format
)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}

i = 1
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

logging.info("Starting the scraping process.")

with open('books_dataset.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Price', 'Rating', 'Availability'])
    while True:
        url = f"https://books.toscrape.com/catalogue/page-{i}.html"        
        try:
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.content, 'lxml')            
            logging.info(f"Page {i} retrieved successfully.")           
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error on page {i}: {e}. Retrying in 5 seconds.")            
            time.sleep(5)
            continue        
        try:
            articles = soup.find_all('article', class_='product_pod')           
            for article in articles:
                title = article.h3.a['title']
                price = float(article.find('p', class_='price_color').text.replace('£', ''))
                rating_word = article.find('p', class_='star-rating')['class'][1]
                rating = rating_map.get(rating_word, "Unknown")
                availability = article.find('p', class_='instock availability').text.strip()
                writer.writerow([title, price, rating, availability])
        except Exception as e:
            logging.warning(f"Error parsing page {i}: {e}")       
        
        next_button = soup.select_one('li.next > a')
        if not next_button:
            logging.info("No more pages to scrape. Ending the process.")
            break
        time.sleep(1)
        i += 1
        
 # The version with SQLite database will come soon!