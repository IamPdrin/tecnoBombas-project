from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

from tecnoApp.models import Documentos, Equipamentos
from tecnoApp.forms import FormEquipamento, FormDocumento


def landing_page(request):
    return render(request, 'landingPage.html')

def main(request):
    return render(request, 'principal.html')

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

