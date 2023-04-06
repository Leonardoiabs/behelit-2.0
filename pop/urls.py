from django.urls import path
from pop.views import *

urlpatterns = [
    path('', QuadrinhosList.as_view(), name='quadrinhos_list'),
    path('add/', QuadrinhosCreate.as_view(), name='quadrinhos_add'),
    path('update/<int:pk>/', QuadrinhosUpdate.as_view(), name='quadrinhos_update'),
    path('delete/<int:pk>/', QuadrinhosDelete.as_view(), name='quadrinhos_delete'),
    path('detail/<int:pk>/', QuadrinhosDetail.as_view(), name='quadrinhos_detail'),

    path('lista_livros/', LivrosList.as_view(), name='livros_list'),
    path('add_livros/', LivrosCreate.as_view(), name='livros_add'),
    path('update_livros/<int:pk>/', LivrosUpdate.as_view(), name='livros_update'),
    path('delete_livros/<int:pk>/', LivrosDelete.as_view(), name='livros_delete'),
    path('detail_livros/<int:pk>/', LivrosDetail.as_view(), name='livros_detail'),

    path('lista_jogos_eletronicos/', JogosEletronicosList.as_view(), name='jogos_eletronicos_list')

]
