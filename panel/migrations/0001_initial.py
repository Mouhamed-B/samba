# Generated by Django 3.1.3 on 2020-11-04 16:46

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('legal_status', models.CharField(choices=[('IND', 'l’Entreprise individuelle'), ('GIE', 'le GIE '), ('SARL', 'la Société à Responsabilité Limitée'), ('SA', 'la Société anonyme'), ('SNC', 'la Société en Nom Collectif'), ('SCS', 'la Société en Commandite Simple'), ('SC', 'la société civile'), ('SCoo', 'la société coopérative')], default=('SC', 'la société civile'), max_length=100, verbose_name='Statut légal')),
                ('address', models.CharField(max_length=200, verbose_name='Addresse')),
                ('phone', models.CharField(max_length=200, verbose_name='Téléphone')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date inscription')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Dernière modification')),
            ],
            options={
                'verbose_name': 'Entreprise',
                'verbose_name_plural': 'Entreprises',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('avatar', models.ImageField(max_length=200, upload_to=None, verbose_name='Avatar')),
                ('civility', models.CharField(choices=[('Mr', 'Monsieur'), ('Mlle', 'Mademoiselle'), ('Mme', 'Madame')], max_length=12, verbose_name='Civilité')),
                ('address', models.CharField(max_length=200, verbose_name='Addresse')),
                ('phone', models.CharField(max_length=200, verbose_name='Téléphone')),
                ('has_company', models.BooleanField(default=False, verbose_name='Est gérant')),
                ('companies', models.ManyToManyField(to='panel.Enterprise', verbose_name='Compagnies')),
            ],
            options={
                'verbose_name': 'Utilisateur',
                'verbose_name_plural': 'Utilisateurs',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='enterprise',
            name='staff',
            field=models.ManyToManyField(to='panel.User', verbose_name='Staff'),
        ),
    ]
