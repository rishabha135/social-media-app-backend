# Generated by Django 3.1.1 on 2020-09-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileDetails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledetail',
            name='lastactive',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
