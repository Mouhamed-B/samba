# Generated by Django 3.1.3 on 2020-11-17 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_auto_20201114_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(max_length=200, null=True, upload_to='static/images/avatar/', verbose_name='Avatar'),
        ),
    ]
