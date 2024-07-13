from django.shortcuts import render

from Tasks.models import Tasks

from django import forms

import calendar
from datetime import datetime

# Create your views here.

menu = {
    'Задачи':'index',
    'Логин':'',
    'Регистрация':'',

}

def calendar_view():
    # Получаем текущую дату
    now = datetime.now()
    year = now.year
    month = now.month
    today = now.day

    # Создаем объект HTMLCalendar и генерируем HTML для текущего месяца
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    month_calendar = cal.formatmonth(year, month)

    # Добавляем класс CSS для выделения текущего дня
    month_calendar = month_calendar.replace(f'>{today}<', f' class="today">{today}<')
    return month_calendar



def show_index(request):
    tasks = Tasks.objects.all()

    data = {

        'menu': menu,
        'tasks':tasks,
        'calendar': calendar_view(),

    }
    return render(request, 'Tasks/index.html', data)
