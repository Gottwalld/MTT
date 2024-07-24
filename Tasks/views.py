from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from Tasks.forms import AddPostForm
from Tasks.models import Tasks

from django import forms

# Create your views here.

menu = [{'title':'Задачи', 'url_name':'index'},
    {'title': 'Войти', 'url_name': 'login'},
    {'title': 'Регистрация', 'url_name': 'registration_page'},]



def show_index(request):
    tasks = Tasks.objects.all()

    data = {

        'menu': menu,
        'tasks':tasks,

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

    return render(request, 'Tasks/add-task.html', {'form': form,})
def login_page(request):
    return HttpResponse('Страница логина')

def registration_page(request):
    return render(request, 'Tasks/registration.html')
