from django.urls import path, include
from servicios import views
from django.conf.urls import include, url


# hay que registrar la url de busqueda para que los archivos jpg puedan verse
from django.conf import settings
from django.conf.urls.static import static
from servicios import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('servicios/', views.Servicios, name='servicios'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)