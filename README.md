# books-scraper-python
Web scraper Python pour books.toscrape avec export CSV
# 📚 Books Scraper — Python

A Python web scraper that extracts complete book data from 
[books.toscrape.com](http://books.toscrape.com) and stores 
it locally for analysis.

## ⚙️ Features

- Scrapes all 1000+ books across all categories
- Extracts title, price, rating and availability for each book
- Exports structured data to CSV
- Generates a detailed log file tracking every scraping event
- Includes request delay management to avoid server overload

## 🔧 Technologies

| Library | Role |
|---|---|
| `requests` | HTTP requests to fetch pages |
| `BeautifulSoup4` | HTML parsing and data extraction |
| `csv` | Data export to CSV format |
| `logging` | Event tracking and error logging |
| `time` | Delay management between requests |

## 🚀 How to Run

1. Clone this repository
   git clone https://github.com/ton-username/books-scraper-python

2. Install dependencies
   pip install requests beautifulsoup4

3. Run the scraper
   python finalProjectBookToScrap.py

## 📁 Output

- `books_dataset.csv` — All extracted book data
- `scraping.log` — Full event history

## 👤 Author

**Bellamy30** — Computer Science Student  
University of Douala, Cameroon  
Self-taught in Python, data scraping and automation
