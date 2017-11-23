""" Register model to make it appear on Admin site """
from django.contrib import admin
from app.models import Agenda


class AgendaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Agenda, AgendaAdmin)
