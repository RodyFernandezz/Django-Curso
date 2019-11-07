from django.http import HttpResponse
import datetime
from django.template import Template, Context
# from django.template import loader   - por si solo una plantilla  vas a usar
# Cuadno vas a usar mas de una plantilla
from django.template.loader import get_template
from django.shortcuts import render


class Persona (object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):  # Primera Vista

    p1 = Persona(" Profesor Rody", "Fernandez")
    temasDelCurso = ["Plantillas", "Modelos",
                     "Fomularios", "Vistas", "Despliegues"]
    ahora = datetime.datetime.now()
    # doc_externo = loader.get_template('miplantilla.html') # por si cvas a usar solo una plantilla
    # Por si vas a usar mas de una plantilla
    # doc_externo = get_template('miplantilla.html')
    #document = doc_externo.render({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas": temasDelCurso})
    # return HttpResponse(document)
    return render(request, "miplantilla.html", {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas": temasDelCurso})


def Herramientas(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "Herramientas.html", {"dameFecha": fecha_actual})


def Plomeria(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "Plomeria.html", {"dameFecha": fecha_actual})


def despedida(request):

    return HttpResponse(" Soy Rody ")


def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h3>
    Fecha y Hora actuales %s
    </h3>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)


def calculaEdad(request, edad, anho):
   # edadActual = 18
    periodo = anho-2019
    edadFutura = edad+periodo
    documento = "<html><body><h2> En el año %s tendras %s años" % (
        anho, edadFutura)
    return HttpResponse(documento)
