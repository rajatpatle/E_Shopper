# Generated by Django 4.1.1 on 2022-09-19 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=50)),
                ('ecity', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('esal', models.FloatField()),
                ('edesignation', models.CharField(max_length=50)),
            ],
        ),
    ]