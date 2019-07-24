# Generated by Django 2.2.2 on 2019-07-24 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poupapig', '0004_auto_20190723_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
