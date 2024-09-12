# Register your models here.
from django.contrib import admin
from .models import Cliente, Produto, Venda, ItemVenda, RelatorioVenda

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'descricao', 'preco', 'estoque')

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'quantidade', 'preco', 'data_venda', 'total')

@admin.register(ItemVenda)
class ItemVendaAdmin(admin.ModelAdmin):
    list_display = ('venda', 'produto', 'quantidade', 'preco_venda')

@admin.register(RelatorioVenda)
class RelatorioVendaAdmin(admin.ModelAdmin):
    list_display = ('vendas_mes', 'quant_itens', 'valor_venda')
