from django.db import models

class LinkRed(models.model):
    #Con esto estamos haciendo una clave nosotros
    key = models.SlugField(verbose_name = "Nombre Clave", max_length = 100, unique = True)
    name = models.CharField()
    url = models.URLField(verbose_name = "Enlace", max_length = 200, null = True, blank = True)
    created = models.DateTimeField(auto_now = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"

    def __str__(self): return self.name