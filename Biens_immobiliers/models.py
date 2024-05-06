from django.db import models

class bien_immobilier(models.Model):
    id = models.AutoField(primary_key=True)
    type_bien = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    nombre_chambre = models.CharField(max_length=100)
    nombre_salon = models.CharField(max_length=200)
    parking = models.CharField(max_length=100)
    prix = models.FloatField()
    Proprietaire= models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.type_bien}"
    
class Proprietaire(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nom}"



    
class Locataire(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.nom}"
    
class ContratLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    bien_immobilier = models.ForeignKey(bien_immobilier, on_delete=models.CASCADE)
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    duree = models.PositiveIntegerField()
    loyer_mensuel = models.CharField() 
    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.duree_bail} avec {self.date_debut} et {self.date_fin}"

class Paiement(models.Model):
    id = models.BigAutoField(primary_key=True)
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    contrat_location = models.ForeignKey(ContratLocation, on_delete=models.CASCADE)
    montant_paye = models.FloatField() 
    date_paiement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.montant} avec {self.date_paiement}"

class DemandeLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    bien_immobilier = models.ForeignKey(bien_immobilier, on_delete=models.CASCADE)
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    date_demande = models.DateTimeField(auto_now_add=True)
    etat_demande = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date_demande}"

# Create your models here.
