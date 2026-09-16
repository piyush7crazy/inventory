from django.db import models 

class Inventory(models.Model):
    product=models.CharField(max_length=200)
    stock_quantities=models.IntegerField()
    purchases=models.DecimalField(max_digits=12,decimal_places=2)
    sales=models.DecimalField(max_digits=12,decimal_places=2)
    date_time=models.DateTimeField(auto_now_add=True)
