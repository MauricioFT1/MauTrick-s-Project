# Generated by Django 2.2.7 on 2019-11-28 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_brazilian'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brazilian',
            name='id',
        ),
        migrations.AlterField(
            model_name='brazilian',
            name='name',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
    ]
