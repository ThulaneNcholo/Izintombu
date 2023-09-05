from django.shortcuts import render
from .models import *

# Create your views here.


def IndexView(request):
    return render(request, 'client/index.html')


def ProductDetailsView(request,id):
    productSizes = ['28', '29', '30', '31', '32', '33', '34', '35']
    product = ProductsModel.objects.get(id = id)

    context = {
        "productSizes": productSizes,
        "product" : product
    }
    return render(request, 'products/product_details.html', context)
