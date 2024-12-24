from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):

    """
    This class contains the essential fields and behaviors of the data you are storing.
    Each model maps to a single database table.
    This class is responsible for creating a database table with those attributes.

    """

    user = models.OneToOneField('User', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Purchased(models.Model):


    """
     The fields and actions of the data we're saving are all contained in this class.
     A single database table corresponds to each model. This class is responsible for creating 
     a database table with specified properties.
      
    """
   
    ordered_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        """
        This method will return customer name.
        :param name: self - used to access the attributes and methods of the class in python
        :param type: reference
        :return: str
        
        """
        
        return (self.name)
