import requests
from bs4 import BeautifulSoup
from .models import Author, Quote

def scrape_quotes():
    url = "http://127.0.0.1:8000"  # Локальний сервер
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []
    for quote_block in soup.select("li"):
        text = quote_block.text.split(" - ")[0].strip()
        author_name = quote_block.select_one("a").text.strip()

        author, _ = Author.objects.get_or_create(name=author_name)
        Quote.objects.create(text=text, author=author)

    return len(quotes)
