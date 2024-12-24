
from typing_extensions import Self
from django.conf import DEFAULT_HASHING_ALGORITHM_DEPRECATED_MSG
from unittest.util import _MAX_LENGTH
from django.db import models


#makemigrations: create changes and store in a file.
#migrate: apply the pending changes created by makemigrations.

# Create your models here.
class Wishlist(models.Model):
    """
    This class contains the essential fields and behaviors of the data you are storing.
    Each model maps to a single database table. This class is used to create a database
    table containing those attributes.
    """
     
    category = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    File = models.FileField()
    description =models.TextField(max_length=122)
     
    def __str__(self):
        """
        This method will return product category.
        :param name: self - used to access the attributes and methods of the class in python
        :param type: reference
        :return: str
        """
        return self.category