# Generated by Django 4.2.14 on 2024-07-11 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0002_tasks_task_status_tasks_time_create_tasks_time_end_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='bureaus_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bureau', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='workers',
            name='bureau',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tasks.bureaus_list'),
        ),
    ]