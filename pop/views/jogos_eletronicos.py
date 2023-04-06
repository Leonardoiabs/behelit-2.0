from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from pop.models import JogosEletronicos
from pop.forms.jogos_eletronicos import CadastrarJogoEletronico
from django.urls import reverse_lazy


class JogosEletronicosList(ListView):
    model = JogosEletronicos
    template_name = 'pop/list_jogos_eletronicos.html'
