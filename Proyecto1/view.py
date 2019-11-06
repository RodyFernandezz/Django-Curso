from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template


class Persona (object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):  # Primera Vista

    p1 = Persona(" Profesor Rody", "Fernandez")
    temasDelCurso = ["Plantillas", "Modelos",
                     "Fomularios", "Vistas", "Despliegues"]
    ahora = datetime.datetime.now()
    doc_externo = get_template('miplantilla.html')
    document = doc_externo.render(
        {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas": temasDelCurso})
    return HttpResponse(document)


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
