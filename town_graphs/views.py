from django.http import HttpResponse
from town_graphs.models import Municipio
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, municipio_id):
    municipio = Municipio.objects.get(pk=municipio_id)
    return render_to_response('municipio_detail.html', {'municipio': municipio, 'votos': municipio.votos_set.all().order_by('-num_votos'), 'participacion': municipio.nulos + municipio.blancos + municipio.candidatos})
