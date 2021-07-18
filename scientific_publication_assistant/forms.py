from django import forms
from django.forms import ModelForm

from scientific_publication_assistant.models import PUBLICATION_TYPES, SECTIONS, Publication, Result


class PublicationAddForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255)
    year_of_publication = forms.IntegerField(label="Year of publication")
    citation_full = forms.CharField(label="Full citation")
    citation_text = forms.CharField(label="Citation in text", max_length=64)
    description = forms.CharField(label="Description")
    link = forms.CharField(label="Link", max_length=255)
    topic = forms.CharField(label="Topic", max_length=255)
    section = forms.ChoiceField(label="Section", choices=SECTIONS)


class PublicationEditForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255)
    year_of_publication = forms.IntegerField(label="Year of publication")
    citation_full = forms.CharField(label="Full citation")
    citation_text = forms.CharField(label="Citation in text", max_length=64)
    description = forms.CharField(label="Description")
    link = forms.CharField(label="Link", max_length=255)
    topic = forms.CharField(label="Topic", max_length=255)
    section = forms.ChoiceField(label="Section", choices=SECTIONS)
    id = forms.IntegerField(widget=forms.HiddenInput)


class ResultAddForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255)
    description = forms.CharField(label="Description")
    conclusion = forms.CharField(label="Conclusion")


class ResultEditForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255)
    description = forms.CharField(label="Description")
    conclusion = forms.CharField(label="Conclusion")
    id = forms.IntegerField(widget=forms.HiddenInput)


class MasterPublicationAddForm(forms.Form):
    type = forms.ChoiceField(label="Type", choices=PUBLICATION_TYPES)
    title = forms.CharField(label="Title", max_length=255)
    description = forms.CharField(label="Description")


class LoginForm(forms.Form):
    username = forms.CharField(label="Nazwa użytkownika", max_length=50)
    password = forms.CharField(label="Hasło", max_length=50)


class AddUserForm(forms.Form):
    username = forms.CharField(label="Login", max_length=50)
    email = forms.CharField(label="e-mail", max_length=50)
    password = forms.CharField(label="Hasło", max_length=50)
    repeated_password = forms.CharField(label="Powtórz hasło", max_length=50)
    first_name = forms.CharField(label="Imię", max_length=50)
    last_name = forms.CharField(label="Nazwisko", max_length=50)


class ResetPasswordForm(forms.Form):
    password = forms.CharField(label="Wprowadź nowe hasło", max_length=50)
    repeated_password = forms.CharField(label="Wprowadź ponownie hasło", max_length=50)
