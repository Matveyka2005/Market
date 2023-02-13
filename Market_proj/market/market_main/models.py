from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    phone = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    password1 = models.CharField(max_length=30, verbose_name="Password1")
    password2 = models.CharField(max_length=30, verbose_name="Password2")
    cart = models.OneToOneField("Cart", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
class Cart(models.Model):
    cart_prodct = models.ForeignKey("Product", on_delete=models.CASCADE)
    
    
class Product(models.Model): 
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="photos", null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    