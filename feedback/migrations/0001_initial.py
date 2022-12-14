# Generated by Django 3.2.16 on 2022-11-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='введите ваш текст', verbose_name='текст')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='дата создания', verbose_name='дата создания')),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'вопросы',
            },
        ),
    ]
