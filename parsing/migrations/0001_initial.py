# Generated by Django 4.1.7 on 2023-03-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(default='', max_length=2083, unique=True)),
                ('content', models.CharField(max_length=2083)),
                ('price', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
