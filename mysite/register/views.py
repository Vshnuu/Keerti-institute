from django.shortcuts import render
from .models import Product
from math import ceil
from django.http import HttpResponseRedirect
from .forms import ClientForm

# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    #allProds = [[products, range(1, nSlides), len(products), nSlides]]
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    #params = {'allProds': allProds}
    return render(request, 'register/index.html', params)

def register(request):
    submitted = False
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/class/register?submitted=True')
    else:
        form = ClientForm
        if 'submitted' in request.GET:
            submitted = True

    form = ClientForm
    params = {"form": form, "submitted": submitted}


    return render(request, 'register/register.html' , params)


def product(request, id):
    #Fetch the product using the id
    product = Product.objects.filter(id=id)
    print(product)
    return render(request, 'register/product.html', {'product': product[0]})

