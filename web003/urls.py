from django.contrib import admin
from django.urls import path
from venta import views as views_venta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', views_venta.blog, name = "blog"),
    path('category/<int:category_id>', views_venta.category, name = "category"),
]