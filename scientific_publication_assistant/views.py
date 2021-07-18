from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView

from scientific_publication_assistant.forms import MasterPublicationAddForm, PublicationAddForm, ResultAddForm
from scientific_publication_assistant.models import MasterPublication, PublicationMasterPublication, Publication, \
    Result, ResultMasterPublication


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
        pubs = Publication.objects.filter(masterpublication=master_publication)
        results = Result.objects.filter(masterpublication=master_publication)
        return render(request, 'single_master_publication.html',
                      {"master_publication": master_publication, "pubs": pubs, 'results': results})


class AddPublicationToMasterView(View):
    def get(self, request, id):
        master_publication = MasterPublication.objects.get(id=id)
        form = PublicationAddForm()
        return render(request, 'add_publication_to_master.html',
                      {"form": form, "master_publication": master_publication})

    def post(self, request, id):
        master_publication = MasterPublication.objects.get(id=id)
        form = PublicationAddForm
        publication_title = request.POST.get('title')
        publication_year = request.POST.get('year_of_publication')
        publication_citation_full = request.POST.get('citation_full')
        publication_citation_text = request.POST.get('citation_text')
        publication_description = request.POST.get('description')
        publication_link = request.POST.get('link')
        publication_topic = request.POST.get('topic')
        publication_section = request.POST.get('section')
        p = Publication.objects.create(title=publication_title, year_of_publication=publication_year,
                                       citation_full=publication_citation_full,
                                       citation_text=publication_citation_text,
                                       description=publication_description, link=publication_link,
                                       topic=publication_topic, section=publication_section)
        p.save()
        PublicationMasterPublication.objects.create(publication=p, master_publication=master_publication)
        message = "Publication succesfully added"

        return render(request, 'add_publication_to_master.html',
                      {"form": form, 'message': message, 'master_publication': master_publication})


class AddResultToMasterView(View):
    def get(self, request, id):
        master_publication = MasterPublication.objects.get(id=id)
        form = ResultAddForm()
        return render(request, 'add_result_to_master.html',
                      {"form": form, "master_publication": master_publication})

    def post(self, request, id):
        master_publication = MasterPublication.objects.get(id=id)
        form = ResultAddForm
        result_title = request.POST.get('title')
        result_description = request.POST.get('description')
        result_conclusion = request.POST.get('conclusion')
        r = Result.objects.create(title=result_title, description=result_description, conclusion=result_conclusion)
        r.save()
        ResultMasterPublication.objects.create(result=r, master_publication=master_publication)
        message = "Result succesfully added"
        return render(request, 'add_result_to_master.html',
                      {"form": form, 'message': message, 'master_publication': master_publication})


class EditPublicationView(View):
    def get(self, request, id):
        publication = Publication.objects.get(id=id)
        form = PublicationAddForm(instance=publication)
        return render(request, 'edit_publication.html', {'form': form})

    def post(self, request):
        publication = Publication.objects.get(id=id)
        form = PublicationAddForm(instance=publication)
        p = PublicationAddForm(request.POST, instance=publication)
        p.save()
        message = "Publication succesfully edited"
        return render(request, 'edit_publication.html', {"form": form, 'message': message})
