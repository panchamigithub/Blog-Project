# Generated by Django 2.0.4 on 2018-04-10 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0002_auto_20180409_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]