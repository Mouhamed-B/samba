from django.db import models
from django.urls import reverse
from django.contrib import auth
# Create your models here.

class User(auth.models.User):
    CIVILITY = (
        ('Mr','Monsieur'),
        ('Mlle','Mademoiselle'),
        ('Mme','Madame')
    )

    avatar = models.ImageField(verbose_name="Avatar", upload_to=None, height_field=None, width_field=None, max_length=200)
    civility = models.CharField(verbose_name="Civilité", max_length=12,choices=CIVILITY)
    address = models.CharField(verbose_name="Addresse", max_length=200)
    phone = models.CharField(verbose_name="Téléphone", max_length=200)
    has_company = models.BooleanField(verbose_name="Est gérant", default=False)
    companies = models.ManyToManyField("panel.Enterprise", verbose_name="Compagnies")

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})


class Enterprise(models.Model):
    LEGAL_STATUSES = (
        ('IND','l’Entreprise individuelle'),
        ('GIE','le GIE '),
        ('SARL','la Société à Responsabilité Limitée'),
        ('SA','la Société anonyme'),
        ('SNC','la Société en Nom Collectif'),
        ('SCS','la Société en Commandite Simple'),
        ('SC','la société civile'),
        ('SCoo','la société coopérative')
    )

    name = models.CharField(verbose_name='Nom', max_length=100)
    legal_status = models.CharField(verbose_name='Statut légal', max_length=100, choices=LEGAL_STATUSES, default=LEGAL_STATUSES[6])
    address = models.CharField(verbose_name="Addresse", max_length=200)
    phone = models.CharField(verbose_name="Téléphone", max_length=200)
    created = models.DateTimeField(verbose_name='Date inscription', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Dernière modification', auto_now=True)
    staff = models.ManyToManyField("panel.User", verbose_name="Staff")

    def save(self, *args, **kwargs):
        #save current user in staff
        super(Enterprise, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Entreprise"
        verbose_name_plural = "Entreprises"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("entreprise_detail", kwargs={"pk": self.pk})
