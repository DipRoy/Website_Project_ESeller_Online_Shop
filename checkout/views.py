from django. shortcuts import render, HttpResponse
from django.views.generic import View, TemplateView, CreateView
from .models import *
from django.shortcuts import render, redirect

class CheckoutView (CreateView):
    template_name = "checkout.html"
  
def checkout(request):

    """
    This method will display the checkout page, which will include a cart  and the products that 
    customers have added to their cart. It will collect information from the customer and store it in a
    database.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns checkout page

    """
    if request.user.is_authenticated:
        customer = request.user
        cart, created = 'Cart'.objects.get_or_create(owner=customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cart = []
        cartitems = []
        cart = {'cartquantity': 0}
        context = {'cart': cart, 'cartitems': cartitems}

    return render(request, 'cart/checkout.html', context)