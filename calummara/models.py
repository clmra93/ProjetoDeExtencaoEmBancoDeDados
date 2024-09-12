# Create your models here.
from django.db import models

# Modelo para Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

# Modelo para Produto
class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome_produto

# Modelo para Venda
class Venda(models.Model):
    cliente = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quantidade = models.PositiveBigIntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data_venda = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Venda para {self.cliente}'

# Modelo para ItemVenda
class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome_produto}'

# Modelo para RelatorioVenda
class RelatorioVenda(models.Model):
    vendas_mes = models.IntegerField()
    quant_itens = models.IntegerField()
    valor_venda = models.IntegerField()

    def __str__(self):
        return f"{self.vendas_mes} - {self.valor_venda}"