# Generated by Django 3.2.14 on 2022-08-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_fractionalvalue_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fractionalvalue',
            name='name',
            field=models.FloatField(null=True),
        ),
    ]