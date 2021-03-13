from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def index(request):

    product_objects = Product.objects.all()

    item_name = request.GET.get('item_name')

    if item_name and item_name != '':
        product_objects = product_objects.filter(name__icontains=item_name)

    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    context = {'product_objects': product_objects}

    return render(request, 'shop/index.html', context)
