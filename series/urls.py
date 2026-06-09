from django.urls import path

from . import views

urlpatterns = [

    path(
        "series/",
        views.listar_series
    ),

    path(
        "series/<int:id>/",
        views.buscar_serie
    ),

    path(
        "series/cadastrar/",
        views.cadastrar_serie
    ),

    path(
        "series/atualizar/<int:id>/",
        views.atualizar_serie
    ),

    path(
        "series/excluir/<int:id>/",
        views.excluir_serie
    ),

    path(
        "finalizadas/",
        views.series_finalizadas
    ),

    path(
        "favoritas/",
        views.series_favoritas
    ),
]