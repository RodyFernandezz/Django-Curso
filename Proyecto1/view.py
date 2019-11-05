from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request):  # Primera Vista

    nombre = "Admin"

    apellido = " root"

    ahora = datetime.datetime.now()
    doc_externo = open(
        "K:/Users/Rody\Music/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nombre_persona": nombre,
                   "apellido_persona": apellido, "momento_actual": ahora})

    document = plt.render(ctx)

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
