from django.shortcuts import render
from django.http import HttpResponse
from .models import*
# detection/views.py

from django.http import JsonResponse
from .forms import TransactionForm
from .model import model, label_encoder
from datetime import datetime
import pandas as pd

def index(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # Prepare data for prediction
            amount = form.cleaned_data['amount']
            transaction_date = datetime.strptime(str(form.cleaned_data['transaction_date']), '%Y-%m-%d').timestamp()
            transaction_type = label_encoder.transform([form.cleaned_data['transaction_type']])[0]
            
            new_transaction = pd.DataFrame({
                'Amount': [amount],
                'Transaction Date': [transaction_date],
                'Transaction Type': [transaction_type]
            })
            
            prediction = model.predict(new_transaction)[0]
            result = "Fraud" if prediction == 1 else "Genuine"
            return JsonResponse({'result': result})

    else:
        form = TransactionForm()

    return render(request, 'detection/index.html', {'form': form})


# Create your views here.

def index_page(request):
    return render(request, 'index1.html')

def adm_usr_login(request):
    if request.method == 'POST':
        user_name=request.POST['uname']
        pass_word=request.POST['password']
        try:
            log=login.objects.get(username=user_name,password=pass_word)
            log.save()
            if log.usertype=='admin':
                request.session['lid']=log.pk
                return HttpResponse("<script>alert('login sucessfull');window.location='/admin_page'</script>")
            elif log.usertype=='user':
                request.session['lid']=log.pk
                tch=register.objects.get(loginss=log.pk)
                request.session['userid']=tch.pk
                return HttpResponse("<script>alert('login sucessfull');window.location='/user_page'</script>")
            
        except:
            return HttpResponse("<script>alert('invalid username or password');window.location='/'</script>")
    return render(request, 'login.html')

def thrreg(request):
    if request.method=='POST':
        thr_username=request.POST['username']
        thr_password=request.POST['password']
        thr_firstname=request.POST['firstname']
        thr_lastname=request.POST['lastname']
        thr_place=request.POST['place']
        thr_phone=request.POST['phone']
        thr_email=request.POST['email']
        logs=login(username=thr_username,password=thr_password,usertype='user')
        logs.save()
        teacher_reg=register(firstname=thr_firstname,lastname=thr_lastname,place=thr_place,phone=thr_phone,email=thr_email,loginss=logs)
        teacher_reg.save()

        return HttpResponse("<script>alert('Registration sucessfull');window.location='/index_page'</script>")
    return render(request, 'register.html')

def admin_page(request):
    return render(request, 'adminhome.html')

def user_page(request):
    return render(request, 'userhome.html')



# detection/views.py

def index(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # Prepare data for prediction
            amount = form.cleaned_data['amount']
            transaction_date = datetime.strptime(str(form.cleaned_data['transaction_date']), '%Y-%m-%d').timestamp()
            transaction_type = label_encoder.transform([form.cleaned_data['transaction_type']])[0]
            
            new_transaction = pd.DataFrame({
                'Amount': [amount],
                'Transaction Date': [transaction_date],
                'Transaction Type': [transaction_type]
            })
            
            prediction = model.predict(new_transaction)[0]
            result = "Fraud" if prediction == 1 else "Genuine"
            return JsonResponse({'result': result})

    else:
        form = TransactionForm()

    return render(request, 'detection/index.html', {'form': form})
