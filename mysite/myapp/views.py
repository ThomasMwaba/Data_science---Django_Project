from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Student
import pandas as pd


# Create your views here.
def home(request):
    item = Student.objects.all().values()
    df = pd.DataFrame(item)
    mydict = {"df": df.to_html()}
    return render(request, "index.html", mydict)


def register(request):
    if request.method == "POST":  # checks if  the user has submitted the info
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password == password2:
            if User.objects.filter(email=email).exists():  # checks if the email already exists in the database
                messages.info(request, "Email Already used")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already used")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect("login")

    return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)  # verify the user

        if user is not None:  # checks if the user is on the platform
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Credentials invalid ")
    else:
        return render(request, "login.html")
