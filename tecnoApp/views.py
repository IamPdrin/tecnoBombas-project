from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

from tecnoApp.models import Documentos, Equipamentos, Usuario
from tecnoApp.forms import FormEquipamento, FormDocumento, FormLogin


def landing_page(request):
    return render(request, 'landingPage.html')

def main(request):
    return render(request, 'principal.html')

def login(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            cpf = form.cleaned_data.get('cpf')
            cnpj = form.cleaned_data.get('cnpj')
            senha = form.cleaned_data['senha']
            
            # Verifica o tipo de usuário e a credencial de login (CPF ou CNPJ)
            if tipo == 'PF' and cpf:
                user = authenticate(request, username=cpf, password=senha)
            elif tipo == 'PJ' and cnpj:
                user = authenticate(request, username=cnpj, password=senha)
            else:
                user = None

            if user is not None:
                login(request, user)
                return redirect('home')  # Redireciona para a página inicial ou outra página

            # Se as credenciais forem inválidas
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

        else:
            # Caso o formulário não seja válido
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = FormLogin()
    return render(request, 'login.html')

def get_equipamentos(request):
    equipList = Equipamentos.objects.all().values()
    context = {
        'equipamentos' : equipList
    }
    template = loader.get_template("principal.html")

    return HttpResponse(template.render(context))

def get_documentos(request):
    docList = Documentos.objects.all().values()
    context = {
        'documentos' : docList
    }
    template = loader.get_template("principal.html")

    return HttpResponse(template.render(context))



def excluir_equipamento(request, id_equipamento):
    equipamento = Equipamentos.objects.get(id=id_equipamento)
    equipamento.delete()

    return redirect('principal.html')

def excluir_documento(request, id_documento):
    documento = Documentos.objects.get(id=id_documento)
    documento.delete()

    return redirect('principal.html')


def add_equipamento(request):
    formEquipamento = FormEquipamento(request.POST or None)
    if formEquipamento.is_valid():
        equipamento = formEquipamento.save(commit=False)
        equipamento.usuario = request.user
        formEquipamento.save()

        return redirect('principal.html')
    
    context = {
        'form' : formEquipamento
    }

    return render(request, 'add_equipamento.html', context)

