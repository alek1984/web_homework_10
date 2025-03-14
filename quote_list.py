from django.core.paginator import Paginator

def quote_list(request):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, 10)  # 10 цитат на сторінці
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'quotes/quote_list.html', {'page_obj': page_obj})
