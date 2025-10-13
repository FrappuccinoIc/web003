from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Nombre")
    
    created = models.DateTimeField(auto_now = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de edición")
    
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self): return self.name