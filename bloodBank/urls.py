from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', include('accounts.urls')),
    path('display', views.bloodHome, name = 'bloodHome'),
    path('add-donor', views.addDonor, name= 'addDonor'),
    path('signup', views.signup, name= 'signup'),
    # path('addUser', views.addUser, name= 'addUser'),
    path('signinForm', views.signinForm, name= 'signinForm'),
    # path('signin', views.signin, name= 'signin'),
]