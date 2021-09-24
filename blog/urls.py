
from django.contrib import admin
from django.urls import path
from blog import views
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.blog, name='blog'),

    # si en la url de la pagina colocamos un numero url.py nos toma por defecto como str, en ese caso hay que colocar int:
    path('categorias/<int:categoria_id>/', views.categoria, name='categoria')

]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)