# Generated by Django 3.1.1 on 2020-09-29 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profileDetails', '0007_delete_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountdetail',
            name='Account_id',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='authentication.account'),
            preserve_default=False,
        ),
    ]
