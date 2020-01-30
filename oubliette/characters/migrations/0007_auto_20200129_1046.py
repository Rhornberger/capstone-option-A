# Generated by Django 3.0.2 on 2020-01-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_auto_20200128_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=5000, null=True)),
            ],
            options={
                'ordering': ['note'],
            },
        ),
        migrations.AddField(
            model_name='character',
            name='note',
            field=models.ManyToManyField(to='characters.Note'),
        ),
    ]
