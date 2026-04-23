from django.urls import path

from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('autores/', views.AutorListView.as_view(), name='lista_autores'),
    path('autores/crear/', views.AutorCreateView.as_view(), name='crear_autor'),
    path('autores/editar/<int:pk>/', views.AutorUpdateView.as_view(), name='editar_autor'),
    path('autores/eliminar/<int:pk>/', views.AutorDeleteView.as_view(), name='eliminar_autor'),
    path('libros/', views.LibroListView.as_view(), name='lista_libros'),
    path('libros/crear/', views.LibroCreateView.as_view(), name='crear_libro'),
    path('libros/editar/<int:pk>/', views.LibroUpdateView.as_view(), name='editar_libro'),
    path('libros/eliminar/<int:pk>/', views.LibroDeleteView.as_view(), name='eliminar_libro'),
]
