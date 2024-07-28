import os

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from Tasks.forms import AddPostForm, RegistraionForm
from Tasks.models import Tasks, Workers

from django import forms

# Create your views here.

menu = [{'title': 'Главная страница', 'url_name': 'index'},
        {'title': 'Добавить задачу', 'url_name': 'task_add'},
        {'title': 'Список работников', 'url_name': 'workers_list'},
        {'title': 'Войти', 'url_name': 'login'},
        {'title': 'Регистрация', 'url_name': 'registration_page'},
        ]


def show_index(request):
    tasks = Tasks.objects.all()
    tasks_will_red = Tasks.objects.filter(~Q(task_status='Просрочена') & ~Q(task_status='Выполнена'))

    for task in tasks_will_red:
        if task.time_difference()[0] == '-':
            task.task_status = 'Просрочена'
            task.save()



    data = {

        'menu': menu,
        'tasks': tasks,

    }
    return render(request, 'Tasks/index.html', data)


def task_page(request, pk):
    posts = get_object_or_404(Tasks, pk=pk)

    data = {
        'post': posts,
        'menu': menu,

    }
    return render(request, 'Tasks/task-page.html', data)


def add_task(request):
    form = AddPostForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'Tasks/add-task.html', {'form': form, })


def login_page(request):
    return HttpResponse('Страница логина')


def registration_page(request):
    form = RegistraionForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'Tasks/registration.html', {'form': form, })


def workers_list(request):
    Workerss = Workers.objects.all()
    data = {
        'menu': menu,
        'Workers': Workerss,
    }
    return render(request, 'Tasks/workerslist.html', data)


def show_pass(request):
    return render(request, 'Tasks/saasd.html')
