# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Sum
from .models import Produto, Venda, ItemVenda, Cliente
from django.contrib import messages  # Supondo que você tenha um modelo Produto

def index(request):
    return render(request, 'index.html')

def registro_venda(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        produto_ids = request.POST.getlist('produto')
        quantidade = request.POST.getlist('quantidade')
        preco = request.POST.getlist('preco')
        # Aqui você pode adicionar lógica para salvar a venda no banco de dados
        try:
            cliente = Cliente.objects.get(id=cliente_id)
            total = 0

            #Criar a venda
            venda = Venda(cliente=cliente, total=total)
            venda.save()

            #Criar itens da venda
            for produto_id, quantidade, preco in zip(produto_ids, quantidades, precos):
                produto = Produto.objects.get(id=produto_id)
                item_venda = ItemVenda(venda=venda, produto=produto, quantidade=quantidade, preco_venda=preco)
                item_venda.save()

                #Atualiza o total da venda
                total += float(preco) * int(quantidade)

            #Atualiza o total da venda e salva
            venda.total=total
            venda.save()

            messages.success(request, 'Venda registrada com sucesso!')
            return redirect('index.html') #Redireciona a página inicial
        
        except ValueError as e:
            messages.error(request, f'Erro ao processar os dados: {e}')
        except Cliente.DoesNotExist:
            messages.error(request, 'Cliente não encontrado.')
        except Produto.DoesNotExist:
            messages.error(request, 'Um ou mais produtos não encontrados.')
    

    produtos = Produto.objects.all()
    cliente = Cliente.objects.all()
    return render(request, 'registro_venda.html', {'produtos': produtos})

def controle_estoque(request):
    produtos = Produto.objects.all()
    return render(request, 'controle_estoque.html', {'produtos': produtos})

def relatorio_mensal(request):
    # Obter o mês e ano atuais
    agora = timezone.now()
    mes_atual = agora.month
    ano_atual = agora.year

    # Filtrar as vendas do mês e ano atuais
    vendas_mes = Venda.objects.filter(data_venda__year=ano_atual, data_venda__month=mes_atual)

    # Calcular a quantidade total de vendas
    total_vendas = vendas_mes.count()

    # Calcular a quantidade total de itens vendidos
    total_itens = vendas_mes.aggregate(Sum('quantidade'))['quantidade__sum'] or 0

    # Calcular o valor total das vendas
    valor_total_vendas = vendas_mes.aggregate(Sum('valor_total'))['valor_total__sum'] or 0

    # Contexto para passar para o template
    contexto = {
        'total_vendas': total_vendas,
        'total_itens': total_itens,
        'valor_total_vendas': valor_total_vendas,
    }

    # Renderizar o template com o contexto
    return render(request, 'relatorio_mensal.html', contexto)

def quantidade_em_estoque(request):
    produtos = Produto.objects.all()
    return render(request, 'quantidade_em_estoque.html', {'produtos': produtos})


def adicao_produtos_estoque(request):
    if request.method == 'GET':
        produto_ids = request.GET.getlist('produto')
        quantidade = request.GET.getlist('quantidade')
        preco = request.GET.getlist('preco')

        try:
            produto = Produto.objects.get(id=produto_ids)
            total = 0

            produto_estoque = Produto_estoque(produto=produto, total=total)
            produto_estoque.save()

            messages.success(request, 'Estoque atualizado com sucesso!')
            return redirect('adicao_produtos_estoque.html') #Redireciona a página inicial
        
        except ValueError as e:
            messages.error(request, f'Erro ao processar os dados: {e}')

    produtos = Produto.objects.all()
    return render(request, 'adicao_produtos_estoque.html', {'produtos': produtos})