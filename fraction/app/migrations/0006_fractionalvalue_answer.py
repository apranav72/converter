# Generated by Django 3.2.14 on 2022-08-09 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_fractionalvalue_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fractionalvalue',
            name='answer',
            field=models.CharField(default='1', max_length=200),
        ),
    ]