from django.db import models

# Create your models here.

class CustomUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    #balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.username


class Transaction(models.Model):
    payer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='payer')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)


class Balance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)