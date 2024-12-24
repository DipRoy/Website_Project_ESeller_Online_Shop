from django.db import models
from django.contrib.auth.models import User

# Create your models here.
        
class CartProduct(models.Model):

     
    """
     The fields and actions of the data we're saving are all contained in this class.
     A single database table corresponds to each model. This class is responsible for creating 
     a database table with specified properties.
      
    """
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        """
        This method will return the customer detail.

        :param name: self - used to access the attributes and methods of the class in python
        :param type: reference
        :return: str

        """
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)




    
    
