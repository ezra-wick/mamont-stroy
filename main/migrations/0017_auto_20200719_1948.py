# Generated by Django 3.0.7 on 2020-07-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200716_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text_one',
            field=models.TextField(blank=True, db_index=True, max_length=1000),
        ),
    ]