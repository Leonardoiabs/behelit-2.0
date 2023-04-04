from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from pop.models import Quadrinhos
from pop.forms import CadastrarQuadrinhos
from django.urls import reverse_lazy


class QuadrinhosList(ListView):
    model = Quadrinhos
    template_name = 'pop/list_hq_manga.html'


class QuadrinhosCreate(CreateView):
    model = Quadrinhos
    form_class = CadastrarQuadrinhos
    template_name = 'pop/add_hq_manga.html'
    success_url = reverse_lazy('quadrinhos_list')


class QuadrinhosUpdate(UpdateView):
    model = Quadrinhos
    form_class = CadastrarQuadrinhos
    template_name = 'pop/update_hq_manga.html'
    success_url = reverse_lazy('quadrinhos_list')


class QuadrinhosDelete(DeleteView):
    model = Quadrinhos
    template_name = 'pop/hq_manga_confirm_delete.html'
    success_url = reverse_lazy('quadrinhos_list')


class QuadrinhosDetail(DetailView):
    model = Quadrinhos
    template_name = 'pop/detail_hq_manga.html'
