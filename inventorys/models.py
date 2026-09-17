from django.db import models 

class Inventory(models.Model):
    product=models.CharField(max_length=200)
    stock_quantities=models.IntegerField()


class Purchase(models.Model):
    product=models.ForeignKey(Inventory, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=12 , decimal_places=2)
    date_time=models.DateTimeField(auto_now_add=True)


class Sales(models.Model):
    product=models.ForeignKey(Inventory , on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=12 , decimal_places=2)
    date_time=models.DateTimeField(auto_now_add=True)

    
