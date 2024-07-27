

from django.forms import DateInput, SelectDateWidget

from Tasks.models import Tasks, Workers
from django import forms

class AddPostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    time_end = forms.DateTimeField(label='Дата завершения', widget=SelectDateWidget())
    class Meta:
        model = Tasks
        fields = ['title', 'content', 'responce_worker', 'urgency', 'task_status',  'time_end']


class RegistraionForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = ['first_name', 'last_name', 'surname', 'rang', 'email',  'phone', 'bureau']
