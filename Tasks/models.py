from django.db import models

from datetime import timedelta
from django.utils import timezone
# Create your models here.

class Workers(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    rang = models.ForeignKey(to='rang_list', on_delete=models.SET_NULL, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    bureau = models.ForeignKey(to='bureaus_list', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return ' '.join([self.last_name, self.first_name, self.surname])

class rang_list(models.Model):
    rang = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.rang

class bureaus_list (models.Model):
    bureau = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.bureau

class Tasks(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200, blank=True, null=True)
    responce_worker = models.ForeignKey(Workers, on_delete=models.SET_NULL, null=True)
    urgency = models.CharField(max_length=30, choices=(('Срочно', 'Срочно'), ('Нормально', 'Нормально'), ('Очень срочно', 'Очень срочно')))
    task_status = models.CharField(max_length=30, choices=(('В работе','В работе'), ('Открыта','Открыта'), ('Выполнена','Выполнена'), ('Просрочена','Просрочена')), default='Открыта')
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_end = models.DateTimeField(null=True)


    def time_difference(self):
        if self.time_create and self.time_end:
            time_now = timezone.now()
            difference = self.time_end - time_now

            if time_now > self.time_end:
                difference = time_now - self.time_end
                hours = difference.seconds // 3600
                minutes = (difference.seconds % 3600) // 60
                return f'-{difference.days} дней {hours:02d}:{minutes:02d}'
            else:
                return f'{difference.days} дней {difference.seconds // 3600:02d}:{(difference.seconds % 3600) // 60:02d}'
        return timedelta(seconds=0)  # Возвращаем ноль или другое значение по умолчанию

    def __str__(self):
        return self.title

