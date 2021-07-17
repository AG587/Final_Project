from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView

from scientific_publication_assistant.forms import MasterPublicationAddForm
from scientific_publication_assistant.models import MasterPublication


class WelcomeView(TemplateView):
    template_name = "welcome_view.html"


class AboutView(TemplateView):
    template_name = "about.html"


class MasterPublicationsListView(ListView):
    model = MasterPublication
    template_name = 'master_publication_list.html'
    context_object_name = 'page'
    paginate_by = 2
    queryset = MasterPublication.objects.order_by('-created')


class AddMasterPublicationView(FormView):
    form_class = MasterPublicationAddForm
    template_name = 'add_master_publication.html'
    success_url = 'master_publication_list.html'
