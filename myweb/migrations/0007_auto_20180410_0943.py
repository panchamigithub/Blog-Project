# Generated by Django 2.0.4 on 2018-04-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0006_remove_blog_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='blogp',
            field=models.CharField(default='', max_length=255),
        ),
    ]