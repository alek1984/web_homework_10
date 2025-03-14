from django.shortcuts import redirect
from django.contrib import messages
from .scraper import scrape_quotes

def run_scraper(request):
    count = scrape_quotes()
    messages.success(request, f"Додано {count} нових цитат!")
    return redirect('index')
