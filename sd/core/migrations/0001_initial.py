# Generated by Django 4.2.2 on 2024-05-09 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('standard', models.CharField(max_length=50)),
                ('stream', models.CharField(max_length=50)),
            ],
        ),
    ]
