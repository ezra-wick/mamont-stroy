# Generated by Django 3.0.7 on 2020-07-29 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200729_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_category',
            name='title',
            field=models.CharField(choices=[('Главная', 'Главная страница'), ('Специализция', 'Страница специализации'), ('О компании', 'О нас')], db_index=True, default='Главная', max_length=20),
        ),
    ]
