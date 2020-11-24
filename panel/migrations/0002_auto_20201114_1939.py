# Generated by Django 3.1.3 on 2020-11-14 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(max_length=200, null=True, upload_to=None, verbose_name='Avatar')),
                ('civility', models.CharField(choices=[('Mr', 'Monsieur'), ('Mlle', 'Mademoiselle'), ('Mme', 'Madame')], default=('Mr', 'Monsieur'), max_length=12, verbose_name='Civilité')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='Addresse')),
                ('phone', models.CharField(max_length=200, null=True, verbose_name='Téléphone')),
                ('has_company', models.BooleanField(default=False, verbose_name='Est gérant')),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profils',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='companies',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='enterprise',
            name='staff',
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name='Addresse'),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='phone',
            field=models.CharField(max_length=200, null=True, verbose_name='Téléphone'),
        ),
    ]