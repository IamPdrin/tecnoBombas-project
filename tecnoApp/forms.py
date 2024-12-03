from django import forms
from tecnoApp.models import Equipamentos, Documentos

class FormDocumento(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ('tipo_documento', 'tipo_contrato', 'servico', 'especificacoes', 'incluir_todos_equipamentos')


class FormEquipamento(forms.ModelForm):
    class Meta:
        model = Equipamentos
        fields = ('categoria', 'nome', 'especificacoes', 'foto')

        widgets = {
            'foto' : forms.FileInput(attrs={'accept': 'image/*'})
        }
