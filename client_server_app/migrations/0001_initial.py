# Generated by Django 3.0.3 on 2020-09-02 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service_provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_service', models.CharField(max_length=128)),
                ('service_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_provider_Type', models.CharField(max_length=128)),
            ],
        ),
    ]
