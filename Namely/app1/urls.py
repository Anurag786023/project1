"""Namely URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from .import views

urlpatterns = [
  path('',views.index,name="name"),
  path("showstudent",views.showstudent,name="showstudent"),
  path("removestudent",views.removestudent,name="removestudent"),
  path("addstudent",views.addstudent,name="addstudent"),
  path("findstudent",views.findstudent,name="findstudent"),
  path("removestudent/<int:student_id>",views.removestudent,name="removestudentid") ,
  path('homepage',views.index,name="homepage")
]
