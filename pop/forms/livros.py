from django import forms
from pop.models import Livros


class CadastrarLivros(forms.ModelForm):
    model = Livros
    widgets = {
        'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo', 'required': True}),
        'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo', 'required': True}),
        'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo', 'required': True}),
        'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o link para download'}),
        'descricao': forms.Textarea(attrs={'class': 'form-control', 'type': 'textarea', 'rows': '6'}),
        'status': forms.Select(attrs={'class': 'form-control js-select2'}),
        'tipo': forms.Select(attrs={'class': 'form-control js-select2'}),
    }

    class Meta:
        model = Livros
        widgets = {}
        fields = [
            'nome',
            'genero',
            'autor',
            'descricao',
            'link',
            'foto',
            'status',
        ]
