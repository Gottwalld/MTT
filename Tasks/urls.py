"""
URL configuration for MTT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from Tasks.views import show_index, task_page, login_page, registration_page, add_task, workers_list, show_pass

urlpatterns = [
    path('', show_index, name='index'),
    path('login/', login_page, name='login'),
    path('registration/', registration_page, name='registration_page'),
    path('task/<int:pk>/', task_page, name='task'),
    path('task_add/', add_task, name='task_add'),
    path('workers_list/', workers_list, name='workers_list'),
    path('test/', show_pass, name='test')

]
