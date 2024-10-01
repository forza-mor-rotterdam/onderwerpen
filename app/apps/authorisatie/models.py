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


class BeheerBekijkenPermissie(BasisPermissie):
    naam = "Beheer bekijken"
    codenaam = "beheer_bekijken"


class RechtengroepLijstBekijkenPermissie(BasisPermissie):
    naam = "Rechtengroep lijst bekijken"
    codenaam = "rechtengroep_lijst_bekijken"


class RechtengroepAanmakenPermissie(BasisPermissie):
    naam = "Rechtengroep aanmaken"
    codenaam = "rechtengroep_aanmaken"


class RechtengroepBekijkenPermissie(BasisPermissie):
    naam = "Rechtengroep bekijken"
    codenaam = "rechtengroep_bekijken"


class RechtengroepAanpassenPermissie(BasisPermissie):
    naam = "Rechtengroep aanpassen"
    codenaam = "rechtengroep_aanpassen"


class RechtengroepVerwijderenPermissie(BasisPermissie):
    naam = "Rechtengroep verwijderen"
    codenaam = "rechtengroep_verwijderen"


class OnderwerpLijstBekijkenPermissie(BasisPermissie):
    naam = "Onderwerp lijst bekijken"
    codenaam = "onderwerp_lijst_bekijken"


class OnderwerpAanpassenPermissie(BasisPermissie):
    naam = "Onderwerp aanpassen"
    codenaam = "onderwerp_aanpassen"


class OnderwerpAanmakenPermissie(BasisPermissie):
    naam = "Onderwerp aanmaken"
    codenaam = "onderwerp_aanmaken"


gebruikersgroep_permissies = (
    GebruikerLijstBekijkenPermissie,
    GebruikerAanmakenPermissie,
    GebruikerBekijkenPermissie,
    GebruikerAanpassenPermissie,
    GebruikerVerwijderenPermissie,
    BeheerBekijkenPermissie,
    OnderwerpLijstBekijkenPermissie,
    OnderwerpAanpassenPermissie,
    OnderwerpAanmakenPermissie,
    RechtengroepLijstBekijkenPermissie,
    RechtengroepAanmakenPermissie,
    RechtengroepBekijkenPermissie,
    RechtengroepAanpassenPermissie,
    RechtengroepVerwijderenPermissie,
)

gebruikersgroep_permissie_opties = [
    (p.codenaam, p.naam) for p in gebruikersgroep_permissies
]
permissie_namen = {p.codenaam: p.naam for p in gebruikersgroep_permissies}


class Permissie(models.Model):
    class Meta:
        managed = False
        default_permissions = ()
        permissions = gebruikersgroep_permissie_opties
