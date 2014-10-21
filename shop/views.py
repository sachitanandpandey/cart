from django.shortcuts import render_to_response
from django.template import RequestContext
from shop.models import Product,Brand

# Create your views here.

def ProductALL(request):
    products = Product.objects.all().order_by('name')
    context = {'products':products}
    return render_to_response('productall.html',context,context_instance=RequestContext(request))

def SpecificProduct(request,productslug):
    product = Product.objects.get(slug=productslug)
    context = {'product': product}
    return render_to_response('specificproduct.html',context,context_instance=RequestContext(request))


def SpecificBrand(request,brandslug):
    brand = Brand.objects.get(slug=brandslug)
    products = Product.objects.filter(brand=brand)
    context = {'products':products}
    return render_to_response('specificbrand.html',context,context_instance=RequestContext(request))