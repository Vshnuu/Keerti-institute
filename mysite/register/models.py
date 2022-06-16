from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300, default="")
    product_image = models.ImageField(upload_to="register/images", default="")
    product_contentname1 = models.CharField(max_length=50, blank=True)
    product_content1 = models.TextField(max_length=300, blank=True)
    product_contentname2 = models.CharField(max_length=50, blank=True)
    product_content2 = models.TextField(max_length=300, blank=True)
    product_contentname3 = models.CharField(max_length=50, blank=True)
    product_content3 = models.TextField(max_length=300, blank=True)
    product_duration = models.CharField(max_length=50, default="")
    product_info = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.product_name


class Client(models.Model):
    name =models.CharField('Venu Name', max_length=200)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=25)
    email = models.EmailField('Student Email')
    course =models.TextField(max_length=200)


    def __str__(self):
        return self.name