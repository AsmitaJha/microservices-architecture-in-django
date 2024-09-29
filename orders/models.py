from django.db import models
from microapp.models import CustomUser
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_id = models.IntegerField()  # Stores product ID from Product App

    """***for monolithic we have to do this,
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) ***
    
    and ***for microservices, we have to insert the product_id manually, by getting it through the url of product api***
    """
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by User {self.user}"
