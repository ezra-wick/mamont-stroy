# Generated by Django 3.0.7 on 2020-06-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200606_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='adress',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='second_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]