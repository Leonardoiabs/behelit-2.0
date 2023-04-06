from django import forms
from pop.models import Quadrinhos


class CadastrarQuadrinhos(forms.ModelForm):
    class Meta:
        model = Quadrinhos
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo', 'required': True}),
            'link': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Digite o link para download'}),
            'descricao': forms.Textarea(attrs={'class':'form-control', 'type':'textarea', 'rows':'6'}),
            'status': forms.Select(attrs={'class':'form-control js-select2'}),
            'tipo': forms.Select(attrs={'class':'form-control js-select2'}),
        }

        fields = [
            'nome',
            'link',
            'foto',
            'descricao',
            'status',
            'tipo',
        ]
