from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from panel.models import Profile, Enterprise
from samba.settings import ADS_IMAGES_PATH
# Create your models here.

class Ad(models.Model):

    title = models.CharField(verbose_name='Titre', max_length=200)
    sponsorised = models.BooleanField(verbose_name="Sponsorisé", default=False)
    description = models.TextField(verbose_name='Description')
    image = models.ImageField("Image", upload_to=ADS_IMAGES_PATH, height_field=None, width_field=None, max_length=None)
    category = models.ForeignKey("advert.Category", verbose_name="Catégorie", on_delete=models.CASCADE,null=True)
    is_available = models.BooleanField(verbose_name='Est disponible', default=True)
    created = models.DateTimeField(verbose_name='Date de création', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Dernière modification', auto_now=True)
    author = models.ForeignKey("auth.User", verbose_name="Annonceur", on_delete=models.CASCADE)
    slug = models.SlugField(default='', editable=False, max_length=40, null = False)
    class Meta:
        verbose_name = "Annonce" 
        verbose_name_plural = "Annonces"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ad_detail", kwargs={"pk": self.pk,"slug" :self.slug})
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super(Ad, self).save(*args, **kwargs)



class Category(models.Model):

    title = models.CharField(verbose_name='Libellé', max_length=200, unique=True)
    created = models.DateTimeField(verbose_name='Date de création', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Dernière modification', auto_now=True)
    slug = models.SlugField(default='', editable=False, max_length=40, null = False)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk,"slug" :self.slug})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)