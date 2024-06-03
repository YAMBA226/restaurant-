from django.db import models
from django.urls import reverse

from shop.settings import AUTH_USER_MODEL

# Create your models here.
"""
Product
- Nom
- Prix
- La quantite en stock
- Image


"""


class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)  # represente l'image

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})


#Article (Order)
"""
- Utilisateur
_ Produit
_ Quantité
_ Commandé ou non 
"""
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.Product.name}({self.quantity})"
# Panier (Cart)
"""

- Utilisateur
_ Articles
_ Commandé ou non 
- Date de la commande 
"""

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username