# Generated by Django 3.2.5 on 2021-07-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('love', '0002_growingup'),
    ]

    operations = [
        migrations.AddField(
            model_name='growingup',
            name='photo',
            field=models.FileField(blank=True, default='', upload_to='./media/', verbose_name='图片'),
        ),
    ]