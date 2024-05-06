from django.db import models

class bien_immobilier(models.Model):
    id_bien = models.AutoField(primary_key=True)
    type_bien = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    nombre_chambre = models.AutoField()
    prix = models.FloatField()

    class Proprietaire(models.Model):
    id_proprietaire = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    coordonnees = models.CharField(max_length=200)
    
class Locataire(models.Model):
    id_locataire = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    coordonnees = models.CharField(max_length=200)
    
class ContratLocation(models.Model):
    bien_immobilier = models.ForeignKey(BienImmobilier, on_delete=models.CASCADE)
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    duree_bail = models.PositiveIntegerField()
    loyer_mensuel = models.FloatField() 
    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(auto_now_add=True)

class Paiement(models.Model):
    contrat_location = models.ForeignKey(ContratLocation, on_delete=models.CASCADE)
    montant = models.FloatField() 
    date_paiement = models.DateTimeField(auto_now_add=True)
    mode_paiement = models.CharField(max_length=100)
   

class DemandeReparation(models.Model):
    bien_immobilier = models.ForeignKey(BienImmobilier, on_delete=models.CASCADE)
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    description = models.TextField()
    date_demande = models.DateTimeField(auto_now_add=True)
    etat_demande = models.CharField(max_length=100)
