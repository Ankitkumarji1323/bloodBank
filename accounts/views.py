from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from bloodBank.models import Donor

from ziyad.settings import USE_I18N

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        donors = Donor.objects.all()
        return render(request, 'bloodindex.html', {'donors':donors})
    else:
        if(request.method == 'POST'):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            print(username)
            print(password)
            print(user)
            if user is not None:
                login(request, user)

                # with open('datas.json', 'r') as infile:
                #     data = infile.read()
                #     new_data = data.replace('}{', '},{')
                #     json_data = json.loads(f'[{new_data}]')

                donors = Donor.objects.all()


                return render(request, 'bloodindex.html', {'donors':donors})
                # return redirect("/")
            else:
                messages.info(request,"invalid credentials")
                print("invalid credentials")
                return redirect("./login")
        else:
            return render(request, 'signin.html')
        


def register(request):
    if(request.method == 'POST'):
        name = request.POST["name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if(password1 == password2):
            if(User.objects.filter(username=name).exists()):
                messages.info(request,'Username already taken')
                print("Username already taken")
                return redirect('./register')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'Email already taken')
                print("email already taken")
                return redirect('./register')
            else:
                user = User.objects.create_user(username=name, email=email, password=password1)
                user.save()
                print("user created")
                return redirect('/')
        else:
            print("Password not matching")
            messages.info(request,'Password not matching')
            return redirect('./register')
    else:
        return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('./login')

def addDonor(request):
    return render(request, "bloodHome.html")