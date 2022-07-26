from .views import *
from django.urls import path

urlpatterns = [
    path("login", loginAPI),
    path("register", registerAPI),
    path("logout", logoutAPI),
    path("getuserdetails", getUserDetail),
]
