# Generated by Django 3.0.2 on 2020-01-22 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spell',
            old_name='effect',
            new_name='duration',
        ),
        migrations.AlterField(
            model_name='spell',
            name='description',
            field=models.CharField(max_length=800),
        ),
    ]