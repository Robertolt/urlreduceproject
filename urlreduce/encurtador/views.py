from django.http import HttpResponse

from django.shortcuts import render, redirect

# Create your views here.
from urlreduce.encurtador.models import UrlRedirect, UrlLog


def relatorio(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    url_reduzida = requisicao.build_absolute_uri(f'/{slug}')
    contexto = {
        'reduce': url_redirect,
        'url_reduzida': url_reduzida,
    }
    return render(requisicao, 'encurtador/relatorio.html', contexto)


def redirecionar(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    UrlLog.objects.create(
        origem=requisicao.META.get(''),
        user_agente=requisicao.META.get(''),
        host=requisicao.META.get(''),
        ip=requisicao.META.get(''),
        url_redirect=url_redirect,
    )
    return redirect(url_redirect.destino)
