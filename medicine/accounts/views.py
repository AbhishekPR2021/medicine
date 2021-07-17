from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        name=request.POST['name']
        pswd=request.POST['pass']
        user=auth.authenticate(username=name,password=pswd)
        if user is not None:
            auth.login(request,user)
            return redirect('/medicine')
        else:
            messages.info(request,'Invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        f_name = request.POST['name']
        mail=request.POST['mail']
        pswd = request.POST['pass']
        pswd2 = request.POST['pass2']
        if pswd == pswd2:
            if User.objects.filter(username=f_name).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=f_name, first_name=f_name, password=pswd,email=mail)
                user.save();
                print('user created')
                return redirect('/medicine')
        else:
            print('miss match')
            messages.info(request, 'password incorrect')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
def signout(request):
    auth.logout(request)
    return redirect('/medicine')