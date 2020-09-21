# Generated by Django 3.1.1 on 2020-09-21 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminID', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='bankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CHITNumber', models.IntegerField(max_length=4)),
                ('accountNumber', models.IntegerField(max_length=12)),
                ('branchCode', models.IntegerField(max_length=12)),
                ('bankName', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratePerHour', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='jobTalent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=254)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='talent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CHITNumber', models.IntegerField(max_length=4)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=254)),
                ('race', models.CharField(max_length=20)),
            ],
        ),
    ]
