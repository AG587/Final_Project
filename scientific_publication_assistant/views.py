from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView

from scientific_publication_assistant.forms import MasterPublicationAddForm, PublicationAddForm, ResultAddForm, \
    PublicationEditForm, ResultEditForm, LoginForm
from scientific_publication_assistant.models import MasterPublication, PublicationMasterPublication, Publication, \
    Result, ResultMasterPublication


class WelcomeView(TemplateView):
    template_name = "welcome_view.html"


class AboutView(TemplateView):
    template_name = "about.html"


class MasterPublicationsListView(LoginRequiredMixin, ListView):
    """ A view used to show list of Projects the Team is working on."""

    model = MasterPublication
    template_name = 'master_publication_list.html'
    context_object_name = 'pubs'
    paginate_by = 10
    queryset = MasterPublication.objects.order_by("id")


class AddMasterPublicationView(LoginRequiredMixin, View):
    """ Enables creating a new Project """
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


class SingleMasterPublicationView(LoginRequiredMixin, View):
    """ Single Project panel, a user can add literature,
    notes and prescribe them to specific sections """
    def get(self, request, id):
        master_publication = MasterPublication.objects.get(id=id)
        pubs = Publication.objects.filter(masterpublication=master_publication)
        results = Result.objects.filter(masterpublication=master_publication)
        return render(request, 'single_master_publication.html',
                      {"master_publication": master_publication, "pubs": pubs, 'results': results})


class AddPublicationToMasterView(LoginRequiredMixin, View):
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


class AddResultToMasterView(LoginRequiredMixin, View):
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


class EditPublicationView(LoginRequiredMixin, View):
    def get(self, request, id):
        publication = Publication.objects.get(id=id)
        form = PublicationEditForm(initial={'title': publication.title,
                                            'year_of_publication': publication.year_of_publication,
                                            'citation_full': publication.citation_full,
                                            'citation_text': publication.citation_text,
                                            'description': publication.description,
                                            'link': publication.link,
                                            'topic': publication.topic,
                                            'section': publication.section,
                                            'id': publication.id,
                                            }
                                   )
        return render(request, 'edit_publication.html', {'form': form})

    def post(self, request, id):
        publication = Publication.objects.get(id=id)
        form = PublicationEditForm
        publication.title = request.POST.get('title')
        publication.year_of_publication = request.POST.get('year_of_publication')
        publication.citation_full = request.POST.get('citation_full')
        publication.citation_text = request.POST.get('citation_text')
        publication.description = request.POST.get('description')
        publication.link = request.POST.get('link')
        publication.topic = request.POST.get('topic')
        publication.section = request.POST.get('section')
        publication.save()
        message = "Publication succesfully edited!"

        return render(request, 'edit_publication.html',
                      {"form": form, 'message': message, 'publication': publication})


class EditResultView(LoginRequiredMixin, View):
    def get(self, request, id):
        result = Result.objects.get(id=id)
        form = ResultEditForm(initial={'title': result.title,
                                       'description': result.description,
                                       'conclusion': result.conclusion,
                                       'id': result.id,
                                       }
                              )
        return render(request, 'edit_result.html', {'form': form})

    def post(self, request, id):
        result = Result.objects.get(id=id)
        form = ResultEditForm
        result.title = request.POST.get('title')
        result.description = request.POST.get('description')
        result.conclusion = request.POST.get('conclusion')
        result.save()
        message = "Result succesfully edited!"
        return render(request, 'edit_result.html',
                      {"form": form, 'message': message, 'result': result})


@login_required
def delete_publication_view(request, id):
    publication = Publication.objects.get(id=id)
    publication.delete()
    message = "Publication succesfully deleted!"
    return render(request, 'delete_publication.html',
                  {'message': message, 'publication': publication})


@login_required
def delete_result_view(request, id):
    result = Result.objects.get(id=id)
    result.delete()
    message = "Result succesfully deleted!"
    return render(request, 'delete_publication.html',
                  {'message': message, 'result': result})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username_to_check = form.cleaned_data['username']
            password_to_check = form.cleaned_data['password']
            user = authenticate(username=username_to_check, password=password_to_check)
        if user is not None:
            login(request, user)
            message = "User logged in!"
        else:
            message = "Authentication failed."
        return HttpResponse(message)
