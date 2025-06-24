from django.db import models

# Create your models here.

class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)

class register(models.Model):
    user_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    loginss=models.ForeignKey(login,on_delete=models.CASCADE)

class transcation(models.Model):
    transcation_id=models.AutoField(primary_key=True)
    accountnumber=models.CharField(max_length=100)
    re_accountnumber=models.CharField(max_length=100)
    ifscnumber=models.CharField(max_length=100)
    reciever_name=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    loginsab=models.ForeignKey(login,on_delete=models.CASCADE)




class complaint(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    reg_compaint=models.CharField(max_length=2000)
    logindd=models.ForeignKey(login,on_delete=models.CASCADE)


class sentreply(models.Model):
    sentreply_id=models.AutoField(primary_key=True)
    reply=models.CharField(max_length=2000)
    complaint_a=models.ForeignKey(login,on_delete=models.CASCADE)


class about(models.Model):
    overview=models.CharField(max_length=5000)

