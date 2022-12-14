# Generated by Django 3.2.16 on 2022-12-16 08:27

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', tinymce.models.HTMLField(help_text='введите ваш текст', verbose_name='описание')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='дата создания', verbose_name='дата создания')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'новости',
            },
        ),
    ]
