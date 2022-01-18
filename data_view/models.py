from django.db import models

# Create your models here.

class immo_bien(models.Model):

    id = models.IntegerField(primary_key=True)
    id_lot = models.TextField(null=True)
    nb_piece = models.IntegerField(null=True)
    typologie = models.CharField(max_length=200, null=True)
    prix_tva_reduite = models.CharField(max_length=200, null=True)
    prix_tva_normale = models.FloatField( null=True)
    prix_ht = models.FloatField(null=True)
    prix_m2_ht = models.FloatField(null=True)
    prix_m2_ttc = models.FloatField(null=True)
    orientation = models.CharField(max_length=200, null=True)
    exterieur = models.CharField(max_length=200, null=True)
    balcony = models.BooleanField(null=True)
    garden = models.BooleanField(null=True)
    parking = models.IntegerField(null=True)
    ville = models.CharField(max_length=200, null=True)
    departement = models.CharField(max_length=200, null=True)
    date_fin_programme = models.CharField(max_length=200, null=True)
    adresse_entiere = models.TextField( null=True)
    date_extraction = models.CharField(max_length=200, null=True)
    surface = models.FloatField(blank=True, null=True)
    etage = models.CharField(max_length=20, null=True)
    nom_programme = models.TextField(blank=True)
    promoteur = models.TextField(blank=True)
    

class Meta:
    constraints = [
        models.UniqueConstraint(fields=['id_lot', 
        'nb_piece', 'typologie', 'prix_tva_reduite',
        'prix_tva_normale', 'prix_ht', 'prix_m2_ht', 'prix_m2_ttc',
        'surface', 'etage', 'orientation', 'exterieur', 'balcony', 'garden',
        'parking', 'nom_programme', 'ville', 'departement', 'date_fin_programme',
        'adresse_entiere', 'promoteur', 'date_extraction' ], name='unique_immo_name')
    ]
    db_table = 'immo_bien'

class Contact(models.Model):
    name =models.CharField(max_length=200, default='', null=False)
    email=models.EmailField(max_length=100, default='', null=False)
    subject=models.TextField()
    
def __str__(self):
    return self.name