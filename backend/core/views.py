from django.shortcuts import render
from .api import search_carrefour


def carrefour_search(request):
    return render(request, 'core/carrefour_search.html', {})


def list_carrefour(request):
    if request.method == "GET":
        query = request.GET.get('search')
        print('Searching...', query)
    products = search_carrefour(query)
    print('type -->> ', type(products))
    return render(request, 'core/carrefour_list.html', {'products': products})

