# Generated by Django 2.2.2 on 2019-06-17 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poupapig', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]