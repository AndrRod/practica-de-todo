
from .views import CrearArticulo
from gestionPedidos import views, urls
from django.urls import path



# urlpatterns = [

#     path('indice/', views.index.as_view(), name ='indice'),
#     path('detalle/<pk>', views.detail.as_view(), name ='detalle'),
#     path('<pk>/resulado/', views.results.as_view(), name ='resultado'),
#     path('<question_id>/votar/', views.vote, name ='votar'),
    
#     ]

# cambiando a vistas basaadas en clases



urlpatterns = [

    path('indice/', views.index, name ='indice'),
    path('detalle/<question_id>', views.detail, name ='detalle'),
    path('<question_id>/votar/', views.vote, name ='votar'),
    path('<question_id>/resulado/', views.results, name ='resultado'),
    
   
    
    
    
    path('crear_articulo/', views.CrearArticulo.as_view(), name='CrearArticulo')


# creando otras vistas para ver ejemplo carro de comparas

    
    ]

