# Generated by Django 3.2.20 on 2023-07-25 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20230722_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password1',
        ),
    ]
