from django.db import models

class Product(models.Model):
    """
    This class contains the essential fields and behaviors of the data you’re storing.
    Each model maps to a single database table.

    This class is used to create a database table containg those attributes.
    """
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=400)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="static")

    def __str__(self):
        """
        This method will return products name.
        :param name: self - used to access the attributes and methods of the class in python
        :param type: reference
        :return: str
        """
        return self.product_name
