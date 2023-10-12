"""
Management utility to create superusers.
"""


from apps.categories.models import Category
from apps.groups.models import Group
from django.core.management.base import BaseCommand


class NotRunningInTTYException(Exception):
    pass


PASSWORD_FIELD = "password"


class Command(BaseCommand):
    def handle(self, *args, **options):

        data = [
            {
                "attributes": {
                    "Beheer.Categorie_Hoofdcategorie": {
                        "readonly": True,
                        "value": None,
                    },
                    "Beheer.Categorie_CategorieIcoon": {
                        "readonly": True,
                        "value": "37154696925806698",
                    },
                    "Actief": {"readonly": True, "value": True},
                    "CategorieNaam": {"readonly": True, "value": "Sloten en singels"},
                    "Overig": {"readonly": True, "value": False},
                },
                "guid": "9851624184872974",
                "hash": "cLKRA6sNv+91ujoPgVAOOHlnzIuB42McT9NrSEPaWgA=",
                "objectType": "Beheer.Categorie",
                "onderwerpen": [
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {"readonly": True, "value": "Fontein"},
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872974",
                            },
                        },
                        "guid": "39406496739491979",
                        "hash": "C0fKrdHtI82UUqaC7bLF/Csl33Xrczt+oL/5gDqhl+w=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Kade of kant beschadigd",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872974",
                            },
                        },
                        "guid": "39406496739491960",
                        "hash": "/361yhqteEl9k/UIXVMT3tbkt7zo+N3YAUSghwpBBQA=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Vervuiling in het water",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872974",
                            },
                        },
                        "guid": "39406496739491944",
                        "hash": "nQb97X6/KmRokeWSeCzUXvUcyp7GH7oFQOfRsGGkVYM=",
                        "objectType": "Beheer.Subcategorie",
                    },
                ],
            },
            {
                "attributes": {
                    "Beheer.Categorie_Hoofdcategorie": {
                        "readonly": True,
                        "value": None,
                    },
                    "Beheer.Categorie_CategorieIcoon": {
                        "readonly": True,
                        "value": "37154696925806699",
                    },
                    "Actief": {"readonly": True, "value": True},
                    "CategorieNaam": {"readonly": True, "value": "Verlichting"},
                    "Overig": {"readonly": True, "value": False},
                },
                "guid": "9851624184873064",
                "hash": "0F/0cM6yMBGNj7pG2lzWoYFEYuvHc1qLH98Xk6Hn2D0=",
                "objectType": "Beheer.Categorie",
                "onderwerpen": [
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Verlichting brandt overdag",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": True},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873064",
                            },
                        },
                        "guid": "39406496739492147",
                        "hash": "B0oMy6Wpxz/QhqVus7k/9R7qR0LgPbBQbbpI7pV++lo=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Verlichting beschadigd",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": True},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873064",
                            },
                        },
                        "guid": "39406496739492146",
                        "hash": "fixgqE+g7XBH3+XZgycs78ShseNRnF7UZ1aOrI4p9KY=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Verlichting overig",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": True},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873064",
                            },
                        },
                        "guid": "39406496739492149",
                        "hash": "VnM1PVbzu4xlaSHasR8MC1fJKhJV1z5zbeGQtB+vPdk=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Verlichting doet het niet",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": True},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873064",
                            },
                        },
                        "guid": "39406496739492148",
                        "hash": "qf9vIIgbSaDsdJoFmiGmtnAMIKOodwk1mS2h37Kfv4I=",
                        "objectType": "Beheer.Subcategorie",
                    },
                ],
            },
            {
                "attributes": {
                    "Beheer.Categorie_Hoofdcategorie": {
                        "readonly": True,
                        "value": None,
                    },
                    "Beheer.Categorie_CategorieIcoon": {
                        "readonly": True,
                        "value": "37154696925806700",
                    },
                    "Actief": {"readonly": True, "value": True},
                    "CategorieNaam": {"readonly": True, "value": "Voertuigen"},
                    "Overig": {"readonly": True, "value": False},
                },
                "guid": "9851624184873065",
                "hash": "3ECQ+aIAfDboHGPTpVx4DWBIgNnHjkx6QJNaH424PIw=",
                "objectType": "Beheer.Categorie",
                "onderwerpen": [
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Parkeeroverlast aanhangwagen",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873065",
                            },
                        },
                        "guid": "39406496739491963",
                        "hash": "DlKKf8RV1Dk40oCZAl0FGur5omtnOuP3O293/09X9h8=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Deel(brom-)fiets",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873065",
                            },
                        },
                        "guid": "39406496739492541",
                        "hash": "K/9AXce2g0wwPWqRhqaC7Rn1Z5SqbserTmLhEWWMfi0=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Parkeeroverlast voertuig",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873065",
                            },
                        },
                        "guid": "39406496739491967",
                        "hash": "/gkP8z3Ru0XuFI2TBQheTdxAVc2uuv/C4UjpqljF9Jw=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Parkeeroverlast (brom-)fiets",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873065",
                            },
                        },
                        "guid": "39406496739491971",
                        "hash": "BSQYYqgTI6YMTpSwla6OeMbucp2BDs1ER+qO11/TzYY=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Voertuigwrak",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873065",
                            },
                        },
                        "guid": "39406496739491972",
                        "hash": "F7x9bD+blhnm6tx+uPl1W9SABjgBgTmespnmZtcePjc=",
                        "objectType": "Beheer.Subcategorie",
                    },
                ],
            },
            {
                "attributes": {
                    "Beheer.Categorie_Hoofdcategorie": {
                        "readonly": True,
                        "value": None,
                    },
                    "Beheer.Categorie_CategorieIcoon": {
                        "readonly": True,
                        "value": "37154696925806701",
                    },
                    "Actief": {"readonly": True, "value": True},
                    "CategorieNaam": {"readonly": True, "value": "Wateroverlast"},
                    "Overig": {"readonly": True, "value": False},
                },
                "guid": "9851624184873066",
                "hash": "fPPOINmjc+qLVRR0myrwC6xJDBXgKk6QSQIKJOCynx4=",
                "objectType": "Beheer.Categorie",
                "onderwerpen": [
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Wateroverlast",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873066",
                            },
                        },
                        "guid": "39406496739491969",
                        "hash": "YF3HdbGRnLEjOXNvAFNZVDNTAQX+0PO2ph0+VCuuX8g=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Rioollucht",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873066",
                            },
                        },
                        "guid": "39406496739491970",
                        "hash": "YHTdLAxhjdHRUcFyamajsDiYL02YGFa8vZxsrcQLoG8=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Gemaal of sluis",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873066",
                            },
                        },
                        "guid": "39406496739492341",
                        "hash": "ROl/05KtDIaLxPoGAuRhwf6b/q2Hqouf8qS0S4uZAJQ=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Rioolafvoer verstopt",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873066",
                            },
                        },
                        "guid": "39406496739491945",
                        "hash": "XGV7pB3HN789JjWUKRMg3Hm3D47F/Pl6jcVo5AJ8Sz4=",
                        "objectType": "Beheer.Subcategorie",
                    },
                ],
            },
            {
                "attributes": {
                    "Beheer.Categorie_Hoofdcategorie": {
                        "readonly": True,
                        "value": None,
                    },
                    "Beheer.Categorie_CategorieIcoon": {
                        "readonly": True,
                        "value": "37154696925806702",
                    },
                    "Actief": {"readonly": True, "value": True},
                    "CategorieNaam": {"readonly": True, "value": "Weg, pad en brug"},
                    "Overig": {"readonly": True, "value": False},
                },
                "guid": "9851624184872970",
                "hash": "kyuKg5NQKeVPPpbeilPmnWWcwn73+KVvKzXqh8WvSDc=",
                "objectType": "Beheer.Categorie",
                "onderwerpen": [
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Gat in de weg",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872970",
                            },
                        },
                        "guid": "39406496739491959",
                        "hash": "MSGmYP9RyEA2/ervs+Ns1Sn6B4vphA7PT+gl5eVAJWc=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Bestrating ongelijk of beschadigd",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872970",
                            },
                        },
                        "guid": "39406496739491958",
                        "hash": "YexP3xKjxu5EMO3zNvqli7Etpmwm2QKWMd+Gw4/iPtk=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {"readonly": True, "value": "Gladheid"},
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872970",
                            },
                        },
                        "guid": "39406496739491961",
                        "hash": "g99f5VvQxFw8/wittMYLbAXxDJdbKb6FhVoOyVsZwyg=",
                        "objectType": "Beheer.Subcategorie",
                    },
                ],
            },
            {
                "attributes": {
                    "Beheer.Categorie_Hoofdcategorie": {
                        "readonly": True,
                        "value": None,
                    },
                    "Beheer.Categorie_CategorieIcoon": {
                        "readonly": True,
                        "value": "37154696925806693",
                    },
                    "Actief": {"readonly": True, "value": True},
                    "CategorieNaam": {"readonly": True, "value": "Dieren"},
                    "Overig": {"readonly": True, "value": False},
                },
                "guid": "9851624184873061",
                "hash": "JMnHkQQ0LzxIncbonkVxTiOy1A5gYMb1q3oD4lV4j54=",
                "objectType": "Beheer.Categorie",
                "onderwerpen": [
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Overlast ongedierte",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873061",
                            },
                        },
                        "guid": "39406496739491965",
                        "hash": "WHOFPYK8CXgDCDpTx2z27utYwXY/D3zC/oRi/Vw01zw=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Overlast insecten",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873061",
                            },
                        },
                        "guid": "39406496739491966",
                        "hash": "8W01hTS6g6JKnYNa5mh8uXoxl2A3n/HA3K9Pz4BNYqY=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Dode dieren",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873061",
                            },
                        },
                        "guid": "39406496739491973",
                        "hash": "Rso0MCFeFWBG4TwEN9OvzhrNyp151ePVE4RpJ34obMc=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Uitwerpselen",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873061",
                            },
                        },
                        "guid": "39406496739491974",
                        "hash": "jiTPmttgHqzBHpc8YVRWfGSk94o+qB37RjtknT7xois=",
                        "objectType": "Beheer.Subcategorie",
                    },
                ],
            },
            {
                "attributes": {
                    "Beheer.Categorie_Hoofdcategorie": {
                        "readonly": True,
                        "value": None,
                    },
                    "Beheer.Categorie_CategorieIcoon": {
                        "readonly": True,
                        "value": "37154696925806695",
                    },
                    "Actief": {"readonly": True, "value": True},
                    "CategorieNaam": {"readonly": True, "value": "Groen"},
                    "Overig": {"readonly": True, "value": False},
                },
                "guid": "9851624184873062",
                "hash": "hhU3uMyNYLGvoTXWLiNH3uobZfOYlUqfjpCvBGn4A44=",
                "objectType": "Beheer.Categorie",
                "onderwerpen": [
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {"readonly": True, "value": "Onkruid"},
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873062",
                            },
                        },
                        "guid": "39406496739491947",
                        "hash": "tUlynIEHgRYOt1SsRUhYHHJyrejCo8wZA1fsWuP8Slg=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Blad of bloesem",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873062",
                            },
                        },
                        "guid": "39406496739491946",
                        "hash": "/oAK+9aO11zPaqaPlWXeyS99OOGDd51wyMjF6+gSb04=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {"readonly": True, "value": "Gras"},
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873062",
                            },
                        },
                        "guid": "39406496739491968",
                        "hash": "HJXrUzVM8askDlD49T+DFS1CbajbolGUhWEhjh9JupQ=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {"readonly": True, "value": "Bomen"},
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873062",
                            },
                        },
                        "guid": "39406496739491975",
                        "hash": "8+mzMVNBVVGw++yMJ2F+6TnbninQDZBmu/72uRryEF4=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {"readonly": True, "value": "Planten"},
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873062",
                            },
                        },
                        "guid": "39406496739492041",
                        "hash": "lsovjKDfr99+a0/DrPbhRleOGRjpa2oNT04/0S6kogY=",
                        "objectType": "Beheer.Subcategorie",
                    },
                ],
            },
            {
                "attributes": {
                    "Beheer.Categorie_Hoofdcategorie": {
                        "readonly": True,
                        "value": None,
                    },
                    "Beheer.Categorie_CategorieIcoon": {
                        "readonly": True,
                        "value": "37154696925806696",
                    },
                    "Actief": {"readonly": True, "value": True},
                    "CategorieNaam": {"readonly": True, "value": "Meubilair"},
                    "Overig": {"readonly": True, "value": False},
                },
                "guid": "9851624184873063",
                "hash": "XFdU642RRNHehRbCROBgT20rtEND/+gBCbxNvA0Wy70=",
                "objectType": "Beheer.Categorie",
                "onderwerpen": [
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Sport- of speeltoestel",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873063",
                            },
                        },
                        "guid": "39406496739491951",
                        "hash": "Rn7f8LNzUlXZEb7OBaYeEQpKBAL+BRQ3IHDJ9lIl5vw=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Bank of tafel",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873063",
                            },
                        },
                        "guid": "39406496739491953",
                        "hash": "GxGF5Z3ak2WPmcDBWL1hrtHIWC0QbubsjRGdwppWn2k=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Verkeers- of straatnaambord",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873063",
                            },
                        },
                        "guid": "39406496739491952",
                        "hash": "dHJ9xcM7Ar/LVbJ6DpnuC0UnUzXWkcV6MCioqW4GqV8=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Informatie- of reclamezuil",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873063",
                            },
                        },
                        "guid": "39406496739491955",
                        "hash": "DeIpQS61mxLlvvmm9W//eariCQ4FoK/pVLwjUdvzkhA=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {"readonly": True, "value": "Klok"},
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184873063",
                            },
                        },
                        "guid": "39406496739491954",
                        "hash": "DUMwIGY68EQCRJMGkEMSgclUmDNTw/0DQ2tErMdv/ZA=",
                        "objectType": "Beheer.Subcategorie",
                    },
                ],
            },
            {
                "attributes": {
                    "Beheer.Categorie_Hoofdcategorie": {
                        "readonly": True,
                        "value": None,
                    },
                    "Beheer.Categorie_CategorieIcoon": {
                        "readonly": True,
                        "value": "37154696925806694",
                    },
                    "Actief": {"readonly": True, "value": True},
                    "CategorieNaam": {"readonly": True, "value": "Afval"},
                    "Overig": {"readonly": True, "value": False},
                },
                "guid": "9851624184872962",
                "hash": "uEuC2qphqDYkxGalG9LoVDblJl4jYe4Oqs21sUXJfN0=",
                "objectType": "Beheer.Categorie",
                "onderwerpen": [
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": True,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Wijkcontainer",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872962",
                            },
                        },
                        "guid": "39406496739492442",
                        "hash": "Mm8vzw25iTWxR4sQ4g6eRy+0JtI4ih2r6DVI01G+lX4=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": True,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Afval naast wijkcontainer",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872962",
                            },
                        },
                        "guid": "39406496739491978",
                        "hash": "jU0Q6aOrHIAfHY/ib/Us7Hn+aP5o/onmOTtRW8r4ah8=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Drugsafval",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872962",
                            },
                        },
                        "guid": "39406496739492141",
                        "hash": "1ivkHcrq/LkVpzHEfOAKD62i5shKIaywLVF0PO5JNEc=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Gevaarlijk afval",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872962",
                            },
                        },
                        "guid": "39406496739491964",
                        "hash": "SiwSciD2S31z37ZY4V81GxjHGJ28yrtX0RLwYFfP1mE=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {"readonly": True, "value": "Grofvuil"},
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872962",
                            },
                        },
                        "guid": "39406496739492142",
                        "hash": "+bRANHpVw+HGXJwvvYMoyQD3mG0jlVUdyRcFaW4BYyo=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Huiscontainer",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872962",
                            },
                        },
                        "guid": "39406496739492241",
                        "hash": "I15KEVHDu4UHF+xC2ey6oSnovkoSEl4eAf5rFJ6CLwA=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {
                                "readonly": True,
                                "value": "Zwerfafval",
                            },
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872962",
                            },
                        },
                        "guid": "39406496739491941",
                        "hash": "BHCAP8iCvedny3bHIhBmrCr+caYsc+0d+xaQIpKp5cc=",
                        "objectType": "Beheer.Subcategorie",
                    },
                    {
                        "attributes": {
                            "ToonAdoptantencodeVraag": {
                                "readonly": True,
                                "value": False,
                            },
                            "SubcategorieNaam": {"readonly": True, "value": "Afvalbak"},
                            "ToonLichtmastWidget": {"readonly": True, "value": False},
                            "Actief": {"readonly": True, "value": True},
                            "Beheer.Subcategorie_Categorie": {
                                "readonly": True,
                                "value": "9851624184872962",
                            },
                        },
                        "guid": "39406496739492441",
                        "hash": "9rsYCgkHaxO6TtGaLZ6JThQcOXAugsHMo9FMoxgwHGo=",
                        "objectType": "Beheer.Subcategorie",
                    },
                ],
            },
        ]

        for group in data:
            group_instance = Group.objects.create(
                name=group.get("attributes", {}).get("CategorieNaam", {}).get("value"),
                public_name=group.get("attributes", {})
                .get("CategorieNaam", {})
                .get("value"),
            )
            categories = [
                Category(
                    group=group_instance,
                    name=category.get("attributes", {})
                    .get("SubcategorieNaam", {})
                    .get("value"),
                    public_name=category.get("attributes", {})
                    .get("SubcategorieNaam", {})
                    .get("value"),
                )
                for category in group.get("onderwerpen", [])
            ]
            Category.objects.bulk_create(categories)
