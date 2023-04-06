from django import forms
from pop.models import JogosFisicos

class CadastrarJogoFisicos(forms.ModelForm):
    class Meta:
        model = JogosFisicos
        widgets = {}
        fields = [
            'nome',
            'genero_fisico',
            'foto',
            'descricao',
            'status',
        ]
