from django.contrib import admin
from django.urls import path
from venta import views as views_venta
from core import views as views_core

urlpatterns = [
    path('', views_core.home, name = "home"),
    path('blog/', views_venta.blog, name = "blog"),
    path('category/<int:category_id>', views_venta.category, name = "category"),
    path('admin/', admin.site.urls),
]