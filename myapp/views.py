from django.shortcuts import render,redirect
from .forms import ExpenseForm # for form 
from .models import Expense#for geting all the expenses from the model
from django.db.models import Sum
import datetime
# Create your views here.
# we created 3 views : index , edit and delete 
def index (request):
    if request.method == "POST":
        expense=ExpenseForm(request.POST)#expense will store the post request from the expenseForm 
        if(expense.is_valid()):
            expense.save() #if valid then that data is saved into the database
            return redirect('index')
        else:
         expense = ExpenseForm()

    expenses=Expense.objects.all() #to get all expenses from expense model  , to display in table
    
    total_expenses=expenses.aggregate(Sum('amount'))
    
    #yearly expense from today's date
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = data.aggregate(Sum('amount'))  

    #monthly expense from today's date
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum('amount'))  

    #weekly expense from today's date
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum('amount'))  

    #daily sums
    daily_sums=Expense.objects.filter().values('date').order_by('date').annotate(sum=(Sum('amount')))
    print(daily_sums)

    #categorical sums
    categorical_sums=Expense.objects.filter().values('category').order_by('category').annotate(sum=(Sum('amount')))
    print(categorical_sums)

    expense_form=ExpenseForm()#to import form data 
    return render(request,'myapp/index.html', {'expense_form':expense_form ,'expenses':expenses ,'total_expenses':total_expenses ,'yearly_sum':yearly_sum,'monthly_sum':monthly_sum,'weekly_sum':weekly_sum ,'daily_sums':daily_sums,'categorical_sums':categorical_sums}) #this is actually get requesst this is what happens in get , post is in form    

def edit (request,id):
    expense=Expense.objects.get(id=id)#passed id hai vo yaha id= then expense milega 
    expense_form=ExpenseForm(instance=expense)#direct fill hona chahiye form after puting id
    if request.method=="POST":#the data came after editing now we need to save it so if its post
       expense=Expense.objects.get(id=id)#we want the expense of that id means all the info 
       form = ExpenseForm(request.POST,instance=expense)# we also want the form so the post data and instance as expense
       #now we will check if the form is valid 
       if form.is_valid():#check if form is valid
          form.save()#save it
          return redirect('index')#redirect to index , also mention up in shortcuts redirect
    return render(request,'myapp/edit.html',{'expense_form':expense_form })  

def delete(request,id):
    if request.method=="POST" and 'delete' in request.POST:
       expense=Expense.objects.get(id=id)
       expense.delete()
       return redirect('index')
