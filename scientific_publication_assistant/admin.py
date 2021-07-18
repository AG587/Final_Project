from django.contrib import admin

from scientific_publication_assistant.models import Publication, Result, MasterPublication, \
    PublicationMasterPublication, ResultMasterPublication

admin.site.register(Publication)
admin.site.register(Result)
admin.site.register(MasterPublication)
admin.site.register(PublicationMasterPublication)
admin.site.register(ResultMasterPublication)

