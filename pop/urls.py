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
]
