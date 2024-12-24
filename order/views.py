from django.shortcuts import render
import json
import datetime
from .models import *
from .utils import*



#view function for cart
def processOrder(request):

    """
    This method is used to place order and confrim order.This takes 
    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :param name: product_id - used to find the specific product for update
    :param type: HttpResponse
    :return: JsonResponse whether payment is complete or not
    """
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Orders.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    # if order.shipping == True:
    #     ShippingAddress.objects.create(
    #         customer=customer,
    #         order=order,
    #         address=data['shipping']['address'],
    #         city=data['shipping']['city'],
    #     )

    return JsonResponse('Payment Complete', safe=False)
