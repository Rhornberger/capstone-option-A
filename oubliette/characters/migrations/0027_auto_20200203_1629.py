# Generated by Django 3.0.2 on 2020-02-04 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0026_auto_20200203_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='item',
            new_name='gear',
        ),
    ]
