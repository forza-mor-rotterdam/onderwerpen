from apps.categories.models import Category
from django import forms
from utils.forms import RadioSelect


class CategoryAanpassenForm(forms.ModelForm):
    priority = forms.ChoiceField(
        widget=RadioSelect(
            attrs={
                "class": "list--form-radio-input",
                "data-action": "change->bijlagen#updateImageDisplay",
            }
        ),
        label="Prioriteit",
        choices=(
            (1, "Hoog"),
            (0, "Normaal"),
        ),
        required=True,
    )

    class Meta:
        model = Category
        fields = ("priority",)
