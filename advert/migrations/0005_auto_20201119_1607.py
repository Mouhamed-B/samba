# Generated by Django 3.1.3 on 2020-11-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0004_auto_20201114_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Libellé'),
        ),
    ]
