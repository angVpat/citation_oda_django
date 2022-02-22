from tabnanny import verbose
from django.db import models
from django.forms import DateField


# Create your models here.


# Model de la table paiements
class Auteur(models.Model):

    id_auteur = models.AutoField(
        primary_key=True,
        unique=True
    )

    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    class Meta:
        db_table = 'auteur'
        verbose_name = 'auteur'
        verbose_name_plural = 'auteur'



class Oeuvre(models.Model):
    id_oeuvre = models.AutoField(
        primary_key=True,
        unique=True
    )
    nom_oeuvre = models.CharField(max_length=255,unique=True)
    maison_edition = models.CharField(max_length=255)
    date_parution = models.DateField()
    auteur_id_auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)

    class Meta:
        db_table = 'oeuvre'
        verbose_name = 'oeuvre'


class Citation(models.Model):
    id_citation = models.AutoField(
        primary_key=True,
        unique=True
    )
    label = models.CharField(max_length=255, unique=True)
    laciation = models.TextField()
    oeuvre_id_oeuvre=models.ForeignKey(Oeuvre, on_delete=models.CASCADE)

    class Meta:
        db_table = 'citation'
        verbose_name = 'citation'

class Theme(models.Model):
    id_theme = models.AutoField(
        primary_key=True,
        unique=True
    )
    libelle = models.CharField(max_length=255, unique=True)
    citation_id_citation = models.ManyToManyField(Citation)

    class Meta:
        db_table = 'theme'
        verbose_name = 'theme'

    def str_(self):
        return self.label


from django.db import models

# Create your models here.
