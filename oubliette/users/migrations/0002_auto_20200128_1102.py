# Generated by Django 3.0.2 on 2020-01-28 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='vegvisir.jpg', upload_to='profile_pics'),
        ),
    ]