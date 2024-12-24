from django.db import models
from django.http import JsonResponse
import datetime
from .models import*


# Create your models here.

class Orders(models.Model):

    """
    This class contains the essential fields and behaviors of the data you’re storing.
    Each model maps to a single database table.
    This class is used to create a database table containg those attributes for Orders.
    """

    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    transaction_id = models.CharField(max_length=100, null=True)
  


def get_total(self):
    
    """
    This method will return total amount for orders.
    :param name: self - used to access the attributes and methods of the class in python
    :param type: reference
    :return: total

    """

    orderitems = self.orderitem.set.all()
    total = sum([item.get_total for item in orderitems])
    return total


class OrderItem(models.Model):
    product = models.ForeignKey('Product',on_delete = models.SET_NULL,blank = True,null = True)
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def get_total(self):
        
        """
        This method will return total amount for cart.
        :param name: self - used to access the attributes and methods of the class in python
        :param type: reference
        :return: total
        """
        total = self.product.price*self.quantity
        return total

