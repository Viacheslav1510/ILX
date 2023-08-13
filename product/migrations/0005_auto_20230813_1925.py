# Generated by Django 3.2.20 on 2023-08-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20230813_1904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Vip', 'Vip'), ('Basic', 'Basic')], default='Vip', max_length=5),
        ),
    ]
