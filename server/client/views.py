from django.shortcuts import render
from .models import *
from products.models import *

# Create your views here.


def IndexView(request):
    whyUs = WhyUsModel.objects.all()
    services = Services.objects.all()
    products = ProductsModel.objects.all()

    context = {
        "whyUs": whyUs,
        "services": services,
        "products": products
    }

    return render(request, 'client/index.html', context)
