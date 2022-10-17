import http
from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import Http404

# Create your views here.


def index(request):

    contatos = Contato.objects.order_by('id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 2)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos

    })


def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404("Usuario não esta mais disponivel")
    # verifica se o usuario esta disponivel para exibição se o mesmo nao estiver
    # ele retorna um erro 404

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
