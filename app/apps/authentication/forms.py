from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

Gebruiker = get_user_model()


class GebruikerAanpassenForm(forms.ModelForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        label="Rechten groep",
        required=False,
    )

    class Meta:
        model = Gebruiker
        fields = ("first_name", "last_name", "group")


class GebruikerAanmakenForm(GebruikerAanpassenForm):
    class Meta:
        model = Gebruiker
        fields = (
            "email",
            "first_name",
            "last_name",
            "group",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[
            "email"
        ].help_text = "Gebruik altijd het e-mailadres van de gemeente."
        self.fields[
            "group"
        ].help_text = "Bestaat de juiste rechtengroep voor deze gebruiker niet, maak deze eerst aan."
