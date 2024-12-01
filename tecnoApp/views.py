from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from tecnoApp.models import Usuario


def tecnoApp(request):

    userList = Usuario.objects.all().values()

    context = {
        'usuarios' : userList
    }

    template = loader.get_template("landingPage.html")

    return HttpResponse(template.render(context))



