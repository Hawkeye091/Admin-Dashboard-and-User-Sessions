from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from myapp.forms import UserForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'myapp/index.html')

def register(request):
    registered= False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'myapp/registration.html',{'user_form':user_form,'registered':registered})

def user_login(request):
    if(request.method=='POST'):
        username= request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active: 
                login(request,user)
                request.session['user_name'] = username
                request.session['user_password'] = password
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried login and failed!")
            print("Username:{} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'myapp/login.html',{})
@login_required
def user_logout(request):
    logout(request)
    try:
        del request.session['user_name']
        del request.session['user_password']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are loggedin")

def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")
def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')
def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")
