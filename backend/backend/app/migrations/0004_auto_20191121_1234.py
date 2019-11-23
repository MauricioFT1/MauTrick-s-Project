# Generated by Django 2.2.6 on 2019-11-21 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191118_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth', models.DateField()),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'People',
                'verbose_name_plural': 'Peoples',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='team',
            name='foundation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='stadium',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='coach',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.People'),
        ),
    ]
