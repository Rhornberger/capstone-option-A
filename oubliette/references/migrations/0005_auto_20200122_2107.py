# Generated by Django 3.0.2 on 2020-01-23 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0004_auto_20200122_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]
