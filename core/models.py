# coding: utf8
#
from __future__ import unicode_literals

from django.db import models

class UserRight(models.Model):
    USERRIGHT_ALL = 'A'
    USERRIGHT_ARTICLES = 'P'
    USERRIGHT_NONE = 'N'

    USERRIGHT_CHOICES = (
        (USERRIGHT_ALL, 'Accès total'),
        (USERRIGHT_ARTICLES, 'Accès articles'),
        (USERRIGHT_NONE, 'Accès interdit'),
    )

    login = models.CharField(max_length=10, unique=True)
    right = models.CharField(max_length=1, choices=USERRIGHT_CHOICES)


class BugReport(models.Model):
    STATE_NOT_RESOLVED = 'N'
    STATE_IN_PROGRESS = 'P'
    STATE_RESOLVED = 'R'

    STATE_CHOICES = (
        (STATE_NOT_RESOLVED, 'Non résolu'),
        (STATE_IN_PROGRESS, 'En cours'),
        (STATE_RESOLVED, 'Terminé'),
    )

    state = models.CharField(max_length=1, choices=STATE_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    reporter_name = models.CharField(max_length=255)
    reporter_mail = models.CharField(max_length=255)
    content = models.TextField()


class PeriodeTVA(models.Model):
    debut = models.DateField()
    fin = models.DateField()
    PERIODE_NON_DECLAREE = 'N'
    PERIODE_DECLAREE = 'D'

    PERIODE_CHOICES = (
        (PERIODE_NON_DECLAREE, 'Non déclarée'),
        (PERIODE_DECLAREE, 'Déclarée'),
    )

    state = models.CharField(max_length=1, choices=PERIODE_CHOICES, default='N')

    class Meta:
        abstract = False


class PricedModel(models.Model):
    tva = models.FloatField(default=0) # TVA en decimal, type 5.5, 20...
    prix = models.FloatField(default=0) # prix TTC

    def get_price_without_taxes(self):
        return round(self.prix * (100 / (100 + self.tva)), 2)

    def get_total_taxes(self):
        return round(self.prix - self.get_price_without_taxes(), 2)

    class Meta:
        abstract = True
