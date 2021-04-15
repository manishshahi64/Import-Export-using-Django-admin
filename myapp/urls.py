from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import AdminView

urlpatterns = [

    path("",AdminView.as_view(),name="admin"),

]