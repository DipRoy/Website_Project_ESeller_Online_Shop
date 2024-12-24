from django.db import models


class AboutUs(models.Model):
    """
    This class contains the essential fields and behaviors of the data you are storing.
    Each model maps to a single database table. This class is used to create a database
    table containing those attributes.
    """
    
    about_us = models.CharField(max_length = 1000)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    is_open = models.BooleanField(default = False)

    def __str__(self):
        """
        This method will return about_us.
        :param name: self - used to access the attributes and methods of the class in python
        :param type: reference
        :return: str
        """
        return self.about_us
