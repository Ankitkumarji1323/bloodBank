from django.db import models
import json

# Create your models here.

class Donor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    blood = models.CharField(max_length=20)
    age = models.IntegerField()

# class signin():
#     email : str
#     password : str
#     with open('signin.json', 'r') as infile:
#         data = infile.read()
#         new_data = data.replace('}{', '},{')
#         json_data = json.loads(f'[{new_data}]')
    
#     if json_data.email == email and json_data.password == password:
#         user = 1
#     else:
#         user = 0