# Generated by Django 2.0.4 on 2018-04-10 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0005_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog',
        ),
    ]