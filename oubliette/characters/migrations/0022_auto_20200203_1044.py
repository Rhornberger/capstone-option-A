# Generated by Django 3.0.2 on 2020-02-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0021_auto_20200203_1042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gear',
            options={'ordering': ['item', 'item_wt', 'item_cost', 'item_type']},
        ),
        migrations.AddField(
            model_name='gear',
            name='item_type',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]