from django.db import models
from django.urls import reverse
from panel.models import User, Enterprise
# Create your models here.

class Ad(models.Model):

    title = models.CharField(verbose_name='Titre', max_length=200)
    description = models.TextField(verbose_name='Description')
    image = models.ImageField("Image", upload_to=None, height_field=None, width_field=None, max_length=None)
    categories = models.ManyToManyField("advert.Category", verbose_name="Catégories")
    is_available = models.BooleanField(verbose_name='Est disponible', default=True)
    created = models.DateTimeField(verbose_name='Date de création', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Dernière modification', auto_now=True)
    author = models.ForeignKey("panel.User", verbose_name="Annonceur", on_delete=models.CASCADE)
    company = models.ForeignKey("panel.Enterprise", verbose_name="Compagnie", on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name = "Annonce"
        verbose_name_plural = "Annonces"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("advertisement_detail", kwargs={"pk": self.pk})

class Category(models.Model):

    title = models.CharField(verbose_name='Libellé', max_length=200)
    ads = models.ManyToManyField("advert.Ad", verbose_name="Liste d'annonces")
    created = models.DateTimeField(verbose_name='Date de création', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Dernière modification', auto_now=True)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})
