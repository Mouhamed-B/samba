# Generated by Django 3.1.3 on 2020-11-05 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='sponsorised',
            field=models.BooleanField(default=False, verbose_name='Sponsorisé'),
        ),
    ]