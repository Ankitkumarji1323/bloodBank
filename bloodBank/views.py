from django.shortcuts import render,redirect
import json

import accounts

from .models import Donor

# Create your views here.
def bloodHome(request):
    donors = Donor.objects.all()
    return render(request, 'bloodindex.html', {'donors':donors})

def addDonor(request):
    if(request.method == 'POST'):
        name = request.POST["Name"]
        Phone = request.POST["Phone"]
        Email = request.POST["Email"]
        blood = request.POST["blood"]
        age = request.POST["age"]

        donor = Donor.objects.create(name=name, phone=Phone,email=Email, blood=blood, age=age)
        donor.save()
        print("donor added")
        return redirect('/')
    else:
        return render(request, 'bloodHome.html')
    # thisdict = {
    #     "name": name,
    #     "phone": Phone,
    #     "email": Email,
    #     "blood": blood,
    #     "age": age,
    # }

    # with open("datas.json", "a") as outfile:
    #     json.dump(thisdict, outfile)

    # with open('datas.json', 'r') as infile:
    #     data = infile.read()
    #     new_data = data.replace('}{', '},{')
    #     json_data = json.loads(f'[{new_data}]')
    


    # return render(request, 'displayBlood.html', {'donors':json_data})


def signup(request):
    return render(request, 'signup.html')

def signinForm(request):
    return render(request, 'signin.html')

# def addUser(request):
#     name = request.POST["name"]
#     phone = request.POST["phone"]
#     email = request.POST["email"]
#     password = request.POST["password"]

#     thisdict = {
#         "name": name,
#         "phone": phone,
#         "email": email,
#         "password": password,
#     }

#     with open("signin.json", "a") as outfile:
#         json.dump(thisdict, outfile)


#     return render(request, 'signin.html')

# def signin(request):
#     email = request.POST["email"]
#     password = request.POST["password"]

#     with open('signin.json', 'r') as infile:
#         data = infile.read()
#         new_data = data.replace('}{', '},{')
#         json_data = json.loads(f'[{new_data}]')
    
#     for i in json_data:
#         userEmail = i["email"]
#         userPassword = i["password"]

#         if userEmail == email and userPassword == password:
#             user = 1
#             break
#         else:
#             user = 0
    


    # return render(request, 'bloodHome.html',{"user":user})