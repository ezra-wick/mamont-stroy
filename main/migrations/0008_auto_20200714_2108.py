# Generated by Django 3.0.7 on 2020-07-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200714_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_four',
            field=models.TextField(blank=True, db_index=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='post',
            name='text_second',
            field=models.TextField(blank=True, db_index=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='post',
            name='text_third',
            field=models.TextField(blank=True, db_index=True, max_length=1000),
        ),
    ]
