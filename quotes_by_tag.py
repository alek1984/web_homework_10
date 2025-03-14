from django.shortcuts import render
from .models import Quote

def quotes_by_tag(request, tag):
    quotes = Quote.objects.filter(tags__contains=[tag])
    return render(request, 'quotes/quote_list.html', {'quotes': quotes, 'tag': tag})
