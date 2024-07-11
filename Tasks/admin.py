from django.contrib import admin

from Tasks.models import Tasks, Workers, rang_list, bureaus_list

# Register your models here.

admin.site.register(Tasks)
admin.site.register(Workers)
admin.site.register(rang_list)
admin.site.register(bureaus_list)