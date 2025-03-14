from collections import Counter
from .models import Quote

def get_top_tags():
    quotes = Quote.objects.all()
    all_tags = [tag for quote in quotes for tag in quote.tags]
    tag_counts = Counter(all_tags)
    return sorted(tag_counts, key=tag_counts.get, reverse=True)[:10]

def index(request):
    quotes = Quote.objects.all()[:10]  # Виведення перших 10 цитат
    top_tags = get_top_tags()
    return render(request, 'quotes/index.html', {'quotes': quotes, 'top_tags': top_tags})
