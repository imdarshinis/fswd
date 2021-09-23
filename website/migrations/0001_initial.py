# Generated by Django 3.2.7 on 2021-09-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250, unique=True)),
                ('number', models.IntegerField(max_length=10, unique=True)),
                ('message', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
