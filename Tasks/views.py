from django.shortcuts import render

from Tasks.models import Tasks

# Create your views here.

menu = {

}


def show_index(request):
    tasks = Tasks.objects.all()

    data = {

        'menu': menu,
        'tasks':tasks,
    }
    return render(request, 'Tasks/index.html', data)
