# Generated by Django 3.2.5 on 2021-07-23 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('love', '0005_alter_growingup_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='growingup',
            name='photo',
        ),
    ]
