import json

from django.http import JsonResponse

from .models import Serie

from django.views.decorators.csrf import csrf_exempt


# Listar tudo
def listar_series(request):

    series = list(
        Serie.objects.values()
    )

    return JsonResponse(
        series,
        safe=False
    )


# Busca por id
def buscar_serie(request, id):

    try:

        serie = Serie.objects.values().get(id=id)

        return JsonResponse(serie)

    except Serie.DoesNotExist:

        return JsonResponse(
            {"erro": "Série não encontrada"},
            status=404
        )


# Criar/cadastrar
@csrf_exempt
def cadastrar_serie(request):

    if request.method != "POST":

        return JsonResponse(
            {"erro": "Método inválido"},
            status=405
        )

    dados = json.loads(request.body)

    serie = Serie.objects.create(
        titulo=dados["titulo"],
        genero=dados["genero"],
        temporadas=dados["temporadas"],
        status=dados["status"],
        nota=dados["nota"]
    )

    return JsonResponse(
        {
            "mensagem": "Série cadastrada com sucesso",
            "id": serie.id
        },
        status=201
    )


# Atualizar
@csrf_exempt
def atualizar_serie(request, id):

    if request.method != "PUT":

        return JsonResponse(
            {"erro": "Método inválido"},
            status=405
        )

    try:

        serie = Serie.objects.get(id=id)

        dados = json.loads(request.body)

        serie.titulo = dados["titulo"]
        serie.genero = dados["genero"]
        serie.temporadas = dados["temporadas"]
        serie.status = dados["status"]
        serie.nota = dados["nota"]

        serie.save()

        return JsonResponse(
            {"mensagem": "Série atualizada com sucesso"}
        )

    except Serie.DoesNotExist:

        return JsonResponse(
            {"erro": "Série não encontrada"},
            status=404
        )


# Deletar
@csrf_exempt
def excluir_serie(request, id):

    if request.method != "DELETE":

        return JsonResponse(
            {"erro": "Método inválido"},
            status=405
        )

    try:

        serie = Serie.objects.get(id=id)

        serie.delete()

        return JsonResponse(
            {"mensagem": "Série removida com sucesso"}
        )

    except Serie.DoesNotExist:

        return JsonResponse(
            {"erro": "Série não encontrada"},
            status=404
        )


# Minhas Finalizadas
def series_finalizadas(request):

    series = list(
        Serie.objects.filter(
            status='FINALIZADA'
        ).values()
    )

    return JsonResponse(
        series,
        safe=False
    )

#Minhas Favoritas
def series_favoritas(request):

    series = list(
        Serie.objects.filter(
            nota=10
        ).values()
    )

    return JsonResponse(
        series,
        safe=False
    )