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


class LivrosUpdate(UpdateView):
    model = Livros
    form_class = CadastrarLivros
    template_name = 'pop/add_livros.html'
    success_url = reverse_lazy('livros_list')


class LivrosDelete(DeleteView):
    model = Livros
    template_name = 'pop/livros_confirm_delete.html'
    success_url = reverse_lazy('livros_list')


class LivrosDetail(DetailView):
    model = Livros
    template_name = 'pop/detail_livros.html'
