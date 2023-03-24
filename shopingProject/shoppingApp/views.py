from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, InvalidPage, EmptyPage


# Create your views here.
def allProductCat(request, c_slug=None):
    c_page = None
    products_list = None

    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.all().filter(category=c_page, availability=True)
    else:
        products_list = Product.objects.all().filter(availability=True)
        pageData = Paginator(products_list, 5)
        try:
            pageNo = int(request.GET.get('page', '1'))
        except:
            pageNo = 1
        try:
            products = pageData.page(pageNo)
        except (EmptyPage, InvalidPage):
            products = pageData.page(pageData.num_pages)
    return render(request, 'category.html', {'category': c_page, 'products': products})


def productDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)

    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})
