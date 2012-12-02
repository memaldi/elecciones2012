from django.http import HttpResponse
from town_graphs.models import Municipio
from django.shortcuts import render_to_response
from django.db.models import Max

def index(request):
    municipios = Municipio.objects.all()
    icons = {}
    votos = {}
    abstencion = {}
    for municipio in municipios:
        votos[municipio.name] = municipio.votos_set.all().order_by('-num_votos')[0]
        abstencion[municipio.name] = (float(municipio.abstenciones) / float(municipio.censo)) * 100
        
    return render_to_response('map.html', {'municipios': municipios, 'votos': votos, 'abstencion': abstencion})

def detail(request, municipio_id):
    municipio = Municipio.objects.get(pk=municipio_id)
    return render_to_response('municipio_detail.html', {'municipio': municipio, 'votos': municipio.votos_set.all().order_by('-num_votos'), 'participacion': municipio.nulos + municipio.blancos + municipio.candidatos})
