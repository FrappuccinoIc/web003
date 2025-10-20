from django.contrib import admin
from .models import LinkRed

class LinkRedAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

# Registra la clase de configuración de permisos admin (LinkRedAdmin) para el modelo LinkRed.
admin.site.register(LinkRed, LinkRedAdmin)