from Tasks.models import Tasks
from django import forms

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'content', 'responce_worker', 'urgency', 'task_status']
