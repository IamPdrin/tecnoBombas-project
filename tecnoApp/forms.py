from django import forms
from tecnoApp.models import Equipamentos, Documentos, Usuario

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

class FormLogin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('tipo', 'cnpj', 'cpf', 'senha')

        widgets = {
            'tipo': forms.RadioSelect(attrs={'class': 'toggle-switch'}),
            'senha': forms.TextInput(attrs={'type': 'password'}),
        }

    def __init__(self, *args, **kwargs):
        super(FormLogin, self).__init__(*args, **kwargs)

        # Modificar o campo CPF/CNPJ dependendo do tipo selecionado
        tipo = self.instance.tipo if self.instance.tipo else 'PF'
        if tipo == 'PF':
            self.fields['cpf'].widget.attrs['placeholder'] = 'CPF'
            self.fields['cnpj'].widget.attrs['placeholder'] = ''
            self.fields['cnpj'].required = False
            self.fields['cpf'].required = True
        else:
            self.fields['cnpj'].widget.attrs['placeholder'] = 'CNPJ'
            self.fields['cpf'].widget.attrs['placeholder'] = ''
            self.fields['cpf'].required = False
            self.fields['cnpj'].required = True