# Generated by Django 3.1.1 on 2020-09-30 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fIndustry', '0007_auto_20200930_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='jobDate',
            field=models.DateField(null=True),
        ),
    ]