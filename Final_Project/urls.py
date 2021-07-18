"""Final_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from scientific_publication_assistant.views import WelcomeView, AboutView, AddMasterPublicationView, \
    MasterPublicationsListView, SingleMasterPublicationView, AddPublicationToMasterView, AddResultToMasterView, \
    EditPublicationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome_view/', WelcomeView.as_view(), name="welcome-view"),
    path('about/', AboutView.as_view(), name="about"),
    path('add_master_publication/', AddMasterPublicationView.as_view(), name="add-master-publication"),
    path('my_publications/', MasterPublicationsListView.as_view(), name="my-publications"),
    path('master_publication/<int:id>/', SingleMasterPublicationView.as_view(), name='single-master-publication'),
    path('add_publication/<int:id>', AddPublicationToMasterView.as_view(),
         name='add-publication-to-master'),
    path('add_result/<int:id>', AddResultToMasterView.as_view(), name='add-result-to-master'),
    path('edit_publication/<int:id>', EditPublicationView.as_view(), name='edit-publication')
]
