# Generated by Django 2.0.4 on 2018-04-10 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0004_auto_20180410_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.CharField(max_length=255)),
                ('uname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myweb.register')),
            ],
        ),
    ]
