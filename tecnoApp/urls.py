from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name="landing_page"),
    path('main', views.main, name="main"),
    path('excluir/<int:id_equipamento>', views.excluir_equipamento, name="excluir_equipamento"),
    path('excluir/<int:id_documento>', views.excluir_documento, name="excluir_documento"),
    path('adicionar-equip', views.add_equipamento, name="add_equipamento"),
    path('login', views.login, name="login"),
]