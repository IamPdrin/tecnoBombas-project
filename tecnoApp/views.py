from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

from tecnoApp.models import Documentos, Equipamentos
from tecnoApp.forms import FormEquipamento, FormDocumento


def landing_page(request):
    return render(request, 'landingPage.html')

def sel_documento(request):
    return render(request, 'sel_documento.html')


def principal(request):
    equipList = Equipamentos.objects.all()
    docList = Documentos.objects.all()
    context = {
        'equipamentos': equipList,
        'documentos': docList,
    }

    template = loader.get_template('principal.html')

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
    formEquipamento = FormEquipamento(request.POST or None, request.FILES or None)

    if formEquipamento.is_valid():
        formEquipamento.save()

        return redirect('principal')
    
    context = {
        'form' : formEquipamento
    }

    return render(request, 'add_equipamento.html', context)

def add_proposta(request):
    formProposta = FormDocumento(request.POST or None)

    if formProposta.is_valid():
        formProposta.save()

        return redirect('sel_documento')
    
    context = {
        'formProposta' : formProposta
    }

    return render(request, 'add_proposta.html', context)


def add_orcamento(request):
    formOrcamento = FormDocumento(request.POST or None)

    if formOrcamento.is_valid():
        formOrcamento.save()

        return redirect('sel_documento')
    
    context = {
        'formOrcamento' : formOrcamento
    }

    return render(request, 'add_orcamento.html', context)


def add_outros(request):
    formOutro = FormDocumento(request.POST or None)

    if formOutro.is_valid():
        formOutro.save()

        return redirect('sel_documento')
    
    context = {
        'formOutro' : formOutro
    }

    return render(request, 'add_outro.html', context)


def edt_equipamento(request, id_equipamento):
    equipamento = Equipamentos.objects.get(id=id_equipamento)

    formEdt = FormEquipamento(request.POST or None, instance=equipamento)
    if request.POST:
        if formEdt.is_valid():
            formEdt.save()
            return redirect('principal')
        
    context = {
        'form' : formEdt
    }
    return render(request, 'edt_equipamento.html', context)


def edt_documento(request, id_documento):
    documento = Documentos.objects.get(id=id_documento)

    formEdtDoc = FormDocumento(request.POST or None, instance=documento)
    if request.POST:
        if formEdtDoc.is_valid():
            formEdtDoc.save()
            return redirect('principal')
        
    context = {
        'form' : formEdtDoc
    }
    return render(request, 'edt_documento.html', context)



