from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('cadastro', views.cadastro, name = 'cadastro'),
    path('debito', views.debito, name = 'debito'),
    path('credito', views.credito, name = 'credito'),
    path('extratoCliente/<cliente_id>', views.extratoCliente, name = 'extratoCliente'),
]
