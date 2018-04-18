from django.urls import path
from .views import listar_clientes, criar_cliente, alterar_cliente, excluir_cliente

urlpatterns = [
    path('', listar_clientes, name='listar_clientes'),
    path('novo', criar_cliente, name='criar_cliente'),
    path('alterar/<int:id>/', alterar_cliente, name='alterar_cliente'),
    path('excluir/<int:id>/', excluir_cliente, name='excluir_cliente'),
]

