from django.forms import ModelForm #for using ModelForm
from .models import Expense #from models import Expense
class ExpenseForm(ModelForm):
    class Meta:
        model=Expense
        #what all feilds we need , no need of date
        fields=('name' , 'amount' , 'category') #now just somehow we have to render this form on our page 
#user will add these 3 feilds int the form and date will get automatically added 