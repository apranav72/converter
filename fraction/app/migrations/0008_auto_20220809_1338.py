# Generated by Django 3.2.14 on 2022-08-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_fractionalvalue_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fractionalvalue',
            name='answer',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fractionalvalue',
            name='name',
            field=models.FloatField(),
        ),
    ]
