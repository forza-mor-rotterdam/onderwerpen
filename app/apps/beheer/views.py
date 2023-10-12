from apps.authentication.forms import GebruikerAanmakenForm, GebruikerAanpassenForm
from apps.categories.forms import CategoryAanpassenForm
from apps.categories.models import Category
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

Gebruiker = get_user_model()


def http_404(request):
    return render(
        request,
        "404.html",
    )


def http_500(request):
    return render(
        request,
        "500.html",
    )


def root(request):
    if request.user.has_perms(["authorisatie.beheer_bekijken"]):
        return redirect(reverse("beheer"))
    return redirect(reverse("account"))


@login_required
def account(request):
    return render(
        request,
        "auth/account.html",
        {},
    )


@permission_required("authorisatie.beheer_bekijken")
def beheer(request):
    return render(
        request,
        "beheer/beheer.html",
        {},
    )


@method_decorator(
    permission_required("authorisatie.gebruiker_bekijken"), name="dispatch"
)
class GebruikerView(View):
    model = Gebruiker
    success_url = reverse_lazy("gebruiker_lijst")


@method_decorator(
    permission_required("authorisatie.gebruiker_lijst_bekijken"), name="dispatch"
)
class GebruikerLijstView(GebruikerView, ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = self.object_list
        context["geauthoriseerde_gebruikers"] = object_list.filter(groups__isnull=False)
        context["ongeauthoriseerde_gebruikers"] = object_list.filter(
            groups__isnull=True
        )
        return context


class GebruikerAanmakenAanpassenView(GebruikerView):
    def form_valid(self, form):
        form.instance.groups.clear()
        if form.cleaned_data.get("group"):
            form.instance.groups.add(form.cleaned_data.get("group"))

        return super().form_valid(form)


@method_decorator(
    permission_required("authorisatie.gebruiker_aanpassen"), name="dispatch"
)
class GebruikerAanpassenView(GebruikerAanmakenAanpassenView, UpdateView):
    form_class = GebruikerAanpassenForm
    template_name = "authentication/gebruiker_aanpassen.html"

    def get_initial(self):
        initial = self.initial.copy()
        obj = self.get_object()
        initial["group"] = obj.groups.all().first()
        return initial


@method_decorator(
    permission_required("authorisatie.gebruiker_aanmaken"), name="dispatch"
)
class GebruikerAanmakenView(GebruikerAanmakenAanpassenView, CreateView):
    template_name = "authentication/gebruiker_aanmaken.html"
    form_class = GebruikerAanmakenForm


@method_decorator(
    permission_required("authorisatie.gebruiker_bekijken"), name="dispatch"
)
class OnderwerpView(View):
    model = Category
    success_url = reverse_lazy("onderwerp_lijst")


@method_decorator(
    permission_required("authorisatie.onderwerp_lijst_bekijken"), name="dispatch"
)
class OnderwerpLijstView(OnderwerpView, ListView):
    queryset = Category.objects.all().order_by("group__name", "name")


@method_decorator(
    permission_required("authorisatie.onderwerp_aanpassen"), name="dispatch"
)
class OnderwerpAanpassenView(OnderwerpView, UpdateView):
    form_class = CategoryAanpassenForm
    template_name = "categories/category_aanpassen.html"

    def get_initial(self):
        initial = self.initial.copy()
        obj = self.get_object()
        initial["priority"] = int(obj.meta.get("priority", 0))
        return initial

    def form_valid(self, form):
        form.instance.meta["priority"] = int(form.cleaned_data.get("priority"))
        return super().form_valid(form)
