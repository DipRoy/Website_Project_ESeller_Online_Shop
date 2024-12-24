from itertools import product
from django.shortcuts import render
from django.template import RequestContext
from .utils import *
from .models import *
# Create your views here.

def search_product(request):
    """
    This method will search product from Product database
    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns base page
    """
    context = {}
   
    data = cartData(request)
    cartItems = data['cartItems']
    context['cartItems'] = cartItems

       
    if request.method == 'GET':
        """
        here i using get method. Get method  request data from server to browser. 

        """
        keyword = request.GET.get('keyword')

        """
        result shows if name,description or category we get in as a keyword. 
        """
        results = Product.objects.filter(name__contains=keyword) | \
                  Product.objects.filter(description__contains=keyword) | \
                  Product.objects.filter(category__contains=keyword) 
    
        context['products'] = results
    else:
        context['products'] = Product.objects.all()
        
        """
        when return data then it return in base.
        """
    return render(request, 'store/base.html', context)



