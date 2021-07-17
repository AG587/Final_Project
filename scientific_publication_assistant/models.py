from django.db import models
from django.forms import ModelChoiceField

PUBLICATION_TYPES = (
    (1, "experimental"),
    (2, "review"),
)

SECTIONS = (
    (1, "introduction"),
    (2, "methods"),
    (3, "results"),
    (4, "conclusions"),
    (5, "discussion"),
)


class Publication(models.Model):
    title = models.CharField(max_length=255)
    year_of_publication = models.IntegerField()
    citation_full = models.TextField()
    citation_text = models.CharField(max_length=64)
    description = models.TextField()
    link = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    section = models.FloatField(choices=SECTIONS)


class Result(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    conclusion = models.TextField()


class MasterPublication(models.Model):
    type = models.FloatField(choices=PUBLICATION_TYPES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publications = models.ManyToManyField(Publication, through="PublicationMasterPublication")
    results = models.ManyToManyField(Result, through="ResultMasterPublication")


class PublicationMasterPublication(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    master_publication = models.ForeignKey(MasterPublication, on_delete=models.CASCADE)


class ResultMasterPublication(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    master_publication = models.ForeignKey(MasterPublication, on_delete=models.CASCADE)

