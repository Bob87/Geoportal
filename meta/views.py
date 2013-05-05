from django.http import HttpResponse
from django.template import Context, loader
from Geoportal.meta.models import Metadatabase

def home(request):
    t = loader.get_template('index.html')
    entries = Metadatabase.objects.all()
    c=Context({'Metadatabase': entries})
    return HttpResponse(t.render(c))
    #return render_to_response('index.html',{'Metadabase': entries})
