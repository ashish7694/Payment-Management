from django.shortcuts import render, redirect
from .models import CustomUser,Transaction,Balance
from django.contrib.auth import authenticate, login
from django.db import models

# Create your views here.

def login_required(home_func):
    def wrapper(request):
        if 'user_id' in request.session:
            return home_func(request)
        else:
            return redirect('login') 
    return wrapper


@login_required
def home(request):
    payer_id = request.session['user_id']
    user_instance = CustomUser.objects.get(id=payer_id)
    try:
        user = Balance.objects.get(user=user_instance)
    except  Balance.DoesNotExist:
        user = 0.0  
    all_transactionhistory = Transaction.objects.filter(payer=user_instance)
    return render(request,'index.html',{'data':user,'all_transactionhistory':all_transactionhistory})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = CustomUser.objects.filter(username=username, password=password)
        
        if users.exists():
            user = users.first()
            request.session['user_id'] = user.id
            return redirect('/home/', {'data': user})
        else:
            error = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error': error})
    else:
        return render(request,'login.html')



def logout_view(request):
    if 'user_id' in request.session:
        request.session.flush()
    return redirect('login') 


@login_required
def add_transaction(request):
    if request.method == 'POST':
        payer_id = request.session['user_id']
        user = CustomUser.objects.get(id=payer_id)
        print('user:-----------',user)
        amount = request.POST['amount']
        transaction = Transaction.objects.create(payer=user, amount=amount)
        
        num_users = CustomUser.objects.count()
        split_amount = float(amount) / num_users
        
        for user in CustomUser.objects.all():
            #if user.id != payer_id:
            Balance.objects.update_or_create(user=user, defaults={'amount': split_amount})
        
        return redirect('transaction_success')
    return render(request, 'add_transaction.html')

@login_required
def transaction_success(request):
    return render(request, 'transaction_success.html')


