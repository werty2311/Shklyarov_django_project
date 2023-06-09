# Generated by Django 4.1.7 on 2023-03-23 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Отзыв')),
                ('email', models.EmailField(max_length=350, verbose_name='Эл.почта')),
                ('text', models.TextField(verbose_name='Содержание')),
                ('date', models.DateField(verbose_name='Дата отзыва')),
                ('time', models.TimeField(verbose_name='Время отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
