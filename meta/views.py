from django.shortcuts import render_to_response

from Geoportal.meta.models import Metadatabase

def home(request):
    entries = Metadatabase.objects.all()
    return render_to_response('index.html',{'Metadabase': entries})
