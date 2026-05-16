import requests
from bs4 import BeautifulSoup
import csv
import time

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
with open('books_dataset.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Price', 'Rating', 'Availability'])
    while True:
        url = f"https://books.toscrape.com/catalogue/page-{i}.html"        
        try:
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.content, 'lxml')            
            print(f"page {i} recuperee avec success.")
        except requests.exceptions.RequestException as e:
            print(f"Alert: {e}.\n Nouvelle tentative dans 5 secondes")
            time.sleep(5)
            continue        
        try:
            articles = soup.find_all('article', class_='product_pod')           
            for article in articles:
                title = article.h3.a['title']
                price = float(article.find('p', class_='price_color').text.replace('£', ''))                
                rating_word = article.find('p', class_='star-rating')['class'][1]  #amelioration de la detection du rating pour plus de robustesse
                rating = rating_map.get(rating_word, "Unknown")
                availability = article.find('p', class_='instock availability').text.strip()
                writer.writerow([title, price, rating, availability])
        except Exception as e:
            print(f"Error parsing page {i}: {e}")    
        
        
        next_button = soup.select_one('li.next > a')     #amelioration de la detection du bouton "next" pour plus de robustesse
        if not next_button:
            break
        time.sleep(1)
        i += 1

### Une version avec base de données SQLite au lieu d'un fichier CSV arrive bientot !