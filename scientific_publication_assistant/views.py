from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView

from scientific_publication_assistant.forms import MasterPublicationAddForm
from scientific_publication_assistant.models import MasterPublication, PublicationMasterPublication


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


class AddMasterPublicationView(View):
    def get(self, request):
        form = MasterPublicationAddForm()
        return render(request, 'add_master_publication.html', {"form": form})

    def post(self, request):
        form = MasterPublicationAddForm(request.POST)
        if form.is_valid():
            publication_type = form.cleaned_data['type']
            publication_title = form.cleaned_data['title']
            publication_description = form.cleaned_data['description']
            MasterPublication.objects.create(type=publication_type, title=publication_title,
                                             description=publication_description)
            message = "Succesfully created"
            return render(request, 'add_master_publication.html', {"form": form, 'message': message})


class SingleMasterPublicationView(View):
    def get(self, request, id):
        master_publication = MasterPublication.objects.get(id=id)
        publications = PublicationMasterPublication.objects.filter(master_publication_id=id)
        ctx = {
            "master_publication": master_publication,
            "publications": publications,
        }
        return render(request, "single_master_publication.html", ctx)
