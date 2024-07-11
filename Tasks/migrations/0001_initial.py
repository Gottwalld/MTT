# Generated by Django 4.2.14 on 2024-07-11 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rang_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rang', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('bureau', models.CharField(blank=True, max_length=30, null=True)),
                ('rang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tasks.rang_list')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, max_length=200, null=True)),
                ('urgency', models.CharField(choices=[('Срочно', 'Срочно'), ('Нормально', 'Нормально'), ('Очень срочно', 'Очень срочно')], max_length=30)),
                ('responce_worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tasks.workers')),
            ],
        ),
    ]
