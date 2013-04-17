from django.http import HttpResponse
from town_graphs.models import Municipio
from django.shortcuts import render_to_response
from django.db.models import Max

def index(request):
    municipios = Municipio.objects.all()
    icons = {}
    votos = {}
    abstencion = {}
    partidos_data_dict = {}
    municipios_dict = {}
    for municipio in municipios:
        municipios_dict[municipio.name] = municipio
        votos[municipio.name] = municipio.votos_set.all().order_by('-num_votos')[0]
        abstencion[municipio.name] = (float(municipio.abstenciones) / float(municipio.censo)) * 100
        for voto in municipio.votos_set.all():
            if voto.num_votos != None:
                if voto.partido.name not in partidos_data_dict.keys():
                    partidos_data_dict[voto.partido.name] = {}
                 
                partidos_data_dict[voto.partido.name][municipio.name] = (float(voto.num_votos) / float(municipio.candidatos)) * 100
        
    return render_to_response('map.html', {'municipios': municipios, 'votos': votos, 'abstencion': abstencion, 'partidos_data_dict': partidos_data_dict, 'municipios_dict': municipios_dict})

def detail(request, municipio_id):
    municipio = Municipio.objects.get(pk=municipio_id)
    return render_to_response('municipio_detail.html', {'municipio': municipio, 'votos': municipio.votos_set.all().order_by('-num_votos'), 'participacion': municipio.nulos + municipio.blancos + municipio.candidatos})
