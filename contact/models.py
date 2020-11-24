from django.db import models

# Create your models here.

class Message(models.Model):
    STATUSES = (
        ('Non lu','Non lu'),
        ('Lu','lu'),
        ('Répondu','Répondu')
    )
    status = models.CharField(max_length=7,default=STATUT[0],choices=STATUT)
    subject = models.CharField(max_length=254, verbose_name="Sujet")
    content = models.TextField(verbose_name='Message')
    name = models.CharField(max_length=80, verbose_name="Nom", null=False)
    surname = models.CharField(max_length=80, verbose_name="Prénom",null=False)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    email = models.EmailField(max_length=254, verbose_name="E-mail",null=False)
    answer = models.TextField(verbose_name='Reponse',default=None,null=True)

    def __str__(self):
        return self.name+' '+self.surname+' : '+self.subject
    
    class Meta:
        ordering = ['-time']

class DirectMessage(models.Model):
    STATUSES = (
        ('Non lu','Non lu'),
        ('Lu','lu'),
        ('Répondu','Répondu')
    )
    status = models.CharField(max_length=7,default=STATUT[0],choices=STATUT)
    content = models.TextField(verbose_name='Message')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    sender = models.ForeignKey("panel.Profile", verbose_name="De ", on_delete=models.CASCADE)
    receiver = models.ForeignKey("panel.Profile", verbose_name="A ", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sender}+ à +self.receiver, {str(self.time)}"
    
    @property
    def time(self):
        """
        renvoie l'heure
        """
        return f"{str(self.time.hour)}:{str(self.time.minute)}"

    @property
    def date(self):
        """
        renvoie la date
        """
        return f"{str(self.time.day)}/{str(self.time.month)}"

    class Meta:
        ordering = ['-timestamp']

