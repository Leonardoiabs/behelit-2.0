from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from pop.models import Livros
from pop.forms import CadastrarLivros
from django.urls import reverse_lazy


class LivrosList(ListView):
    model = Livros
    template_name = 'pop/list_livros.html'


class LivrosCreate(CreateView):
    model = Livros
    form_class = CadastrarLivros
    template_name = 'pop/add_livros.html'
    success_url = reverse_lazy('livros_list')
