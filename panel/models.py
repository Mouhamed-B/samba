from django.db import models
from django.urls import reverse
from samba.settings import AVATAR_PATH
# Create your models here.

class Profile(models.Model):
    CIVILITY = (
        ('Mr','Monsieur'),
        ('Mlle','Mademoiselle'),
        ('Mme','Madame')
    )
    user = models.OneToOneField("auth.User", verbose_name=("Compte"), on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name="Avatar", upload_to=AVATAR_PATH, height_field=None, width_field=None, max_length=200, null=True)
    civility = models.CharField(verbose_name="Civilité", max_length=12,choices=CIVILITY, default=CIVILITY[0])
    address = models.CharField(verbose_name="Addresse", max_length=200, null=True)
    phone = models.CharField(verbose_name="Téléphone", max_length=200, null=True)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profils"

    def __str__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})


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
    avatar = models.ImageField(verbose_name="Avatar", upload_to=AVATAR_PATH, height_field=None, width_field=None, max_length=200, null=True)
    legal_status = models.CharField(verbose_name='Statut légal', max_length=100, choices=LEGAL_STATUSES, default=LEGAL_STATUSES[6])
    address = models.CharField(verbose_name="Addresse", max_length=200, null=True)
    phone = models.CharField(verbose_name="Téléphone", max_length=200, null=True)
    created = models.DateTimeField(verbose_name='Date inscription', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Dernière modification', auto_now=True)
    admin = models.OneToOneField("auth.User", verbose_name="Administrateur", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        #save current profile in staff
        super(Enterprise, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Entreprise"
        verbose_name_plural = "Entreprises"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("entreprise_detail", kwargs={"pk": self.pk})