from django import forms
from pop.models import JogosEletronicos


class CadastrarJogoEletronico(forms.ModelForm):
    class Meta:
        model = JogosEletronicos
        widgets = {}
        fields = [
            'nome',
            'genero_eletronico',
            'foto',
            'descricao',
            'plataforma',
            'status',
        ]
