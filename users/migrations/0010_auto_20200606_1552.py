# Generated by Django 3.0.7 on 2020-06-06 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200606_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer',
            new_name='user',
        ),
    ]
