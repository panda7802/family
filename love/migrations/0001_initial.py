# Generated by Django 3.2.5 on 2021-07-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128, verbose_name='姓名')),
                ('zf', models.CharField(default='', max_length=128, verbose_name='祝福')),
                ('bak_data', models.CharField(blank=True, default='', max_length=1024, verbose_name='备用字段')),
            ],
        ),
    ]
