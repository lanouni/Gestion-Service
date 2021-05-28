from django.db import models
from django.db.models.base import Model

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nom =  models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email =  models.CharField(max_length=64, unique=True)
    mdp = models.CharField(max_length=64)
    tel = models.IntegerField()
    ville = models.CharField(max_length=30)

    def __str__(self):
        return self.nom + " "+self.prenom
    class Meta:
        db_table = "client_client"

class Offre(models.Model):
    date_pub = models.DateTimeField()
    description = models.TextField(max_length=200)
    categorie = models.CharField(max_length=30)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    class Meta:
        db_table = "client_Offre"