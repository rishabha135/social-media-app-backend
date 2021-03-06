# Generated by Django 3.0.3 on 2020-09-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('ph_num', models.CharField(max_length=10, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
