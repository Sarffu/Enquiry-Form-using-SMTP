from django.contrib import admin
from .models import Signals


@admin.register(Signals)
class SiganlAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "mobile", "message"]
