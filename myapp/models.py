from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100) #name of that product 
    amount = models.IntegerField()#amount of that item 
    category=models.CharField(max_length=50)
    date=models.DateField(auto_now=True)#automatically add date to current date 
 
    def __str__(self):
        return self.name