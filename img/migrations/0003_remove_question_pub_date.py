# Generated by Django 4.1.2 on 2023-01-11 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0002_alter_question_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
    ]
