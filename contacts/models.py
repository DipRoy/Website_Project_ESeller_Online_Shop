from django.db import models

# Create your models here.
class Contact(models.Model):
    """
    This class contains the essential fields and behaviors of the data you’re storing.
    Each model maps to a single database table. This class is used to create a database
    table containing those attributes.

    """
    message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100);
    comment = models.TextField(max_length=100)
    date = models.DateField()
    is_replied = models.BooleanField(default=False)

    def __str__(self):
        """
        This method will return customer name.

        :param name: self - used to access the attributes and methods of the class in python
        :param type: reference
        :return: str

        """
        return self.name

class SentReplies(models.Model):
    """
    This class contains the essential fields and behaviors of the data you’re storing.
    Each model maps to a single database table. This class is used to create a database
    table containing those attributes.

    """
    message_sender = models.ForeignKey(Contact,on_delete=models.CASCADE, null=True)
    subject = models.TextField(max_length=100)
    reply = models.TextField(max_length=500)

    def __str__(self):
        """
        This method will return message sender name.

        :param name: self - used to access the attributes and methods of the class in python
        :param type: reference
        :return: str

        """
        return self.message_sender.name