# Generated by Django 2.0.4 on 2018-04-10 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0003_auto_20180410_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
