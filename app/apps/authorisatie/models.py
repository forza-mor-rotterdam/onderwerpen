from django.contrib.gis.db import models


class BasisPermissie:
    naam = None
    codenaam = None


class GebruikerLijstBekijkenPermissie(BasisPermissie):
    naam = "Gebruiker lijst bekijken"
    codenaam = "gebruiker_lijst_bekijken"


class GebruikerAanmakenPermissie(BasisPermissie):
    naam = "Gebruiker aanmaken"
    codenaam = "gebruiker_aanmaken"


class GebruikerBekijkenPermissie(BasisPermissie):
    naam = "Gebruiker bekijken"
    codenaam = "gebruiker_bekijken"


class GebruikerAanpassenPermissie(BasisPermissie):
    naam = "Gebruiker aanpassen"
    codenaam = "gebruiker_aanpassen"


class GebruikerVerwijderenPermissie(BasisPermissie):
    naam = "Gebruiker verwijderen"
    codenaam = "gebruiker_verwijderen"


class GebruikersgroepToekennenPermissie(BasisPermissie):
    naam = "Gebruikersgroep toekennen/verwijderen voor een gebruiker"
    codenaam = "gebruikersgroep_toekennen_verwijderen"


class GebruikersgroepAanmakenPermissie(BasisPermissie):
    naam = "Gebruikersgroep aanmaken"
    codenaam = "gebruikersgroep_aanmaken"


class GebruikersgroepBekijkenPermissie(BasisPermissie):
    naam = "Gebruikersgroep bekijken"
    codenaam = "gebruikersgroep_bekijken"


class GebruikersgroepVerwijderenPermissie(BasisPermissie):
    naam = "Gebruikersgroep verwijderen"
    codenaam = "gebruikersgroep_verwijderen"


class BeheerBekijkenPermissie(BasisPermissie):
    naam = "Beheer bekijken"
    codenaam = "beheer_bekijken"


class OnderwerpLijstBekijkenPermissie(BasisPermissie):
    naam = "Onderwerp lijst bekijken"
    codenaam = "onderwerp_lijst_bekijken"


class OnderwerpAanpassenPermissie(BasisPermissie):
    naam = "Onderwerp aanpassen"
    codenaam = "onderwerp_aanpassen"


gebruikersgroep_permissies = (
    GebruikerLijstBekijkenPermissie,
    GebruikerAanmakenPermissie,
    GebruikerBekijkenPermissie,
    GebruikerAanpassenPermissie,
    GebruikerVerwijderenPermissie,
    GebruikersgroepToekennenPermissie,
    GebruikersgroepAanmakenPermissie,
    GebruikersgroepBekijkenPermissie,
    GebruikersgroepVerwijderenPermissie,
    BeheerBekijkenPermissie,
    OnderwerpLijstBekijkenPermissie,
    OnderwerpAanpassenPermissie,
)

gebruikersgroep_permissie_opties = [
    (p.codenaam, p.naam) for p in gebruikersgroep_permissies
]


class Permissie(models.Model):
    class Meta:
        managed = False
        default_permissions = ()
        permissions = gebruikersgroep_permissie_opties
