from django.urls import path
from . import views  # Importa as views do aplicativo

urlpatterns = [
    path('', views.index, name='index'), # Adiciona uma rota para a view 'index'
    path('registro_venda/', views.registro_venda, name='registro_venda'),
    path('controle_estoque', views.controle_estoque, name='controle_estoque'),
    path('registro_venda/index', views.index, name='index'),
    path('relatorio_mensal', views.relatorio_mensal, name='relatorio_mensal'),
    path('quantidade_em_estoque/', views.quantidade_em_estoque, name='quantidade_em_estoque'),
    path('quantidade_em_estoque/controle_estoque', views.controle_estoque, name='controle_estoque'),
    path('adicao_produtos_estoque', views.adicao_produtos_estoque, name='adicao_produtos_estoque'),
    path('adicao_produtos_estoque/controle_estoque', views.controle_estoque, name='controle_estoque')
]
