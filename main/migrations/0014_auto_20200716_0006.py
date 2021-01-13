# Generated by Django 3.0.7 on 2020-07-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200715_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_category',
            name='title',
            field=models.CharField(choices=[('Главная', 'Главная страница'), ('Специализция', 'Страница специализации')], db_index=True, default='Главная', max_length=20),
        ),
    ]
