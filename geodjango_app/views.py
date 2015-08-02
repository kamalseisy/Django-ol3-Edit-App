from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.template import RequestContext, loader
from django.http import HttpResponse
from geodjango_app.models import HebridesCycle

from django.shortcuts import *
from django.template import RequestContext


def index(request):
    hebrides = HebridesCycle.objects.all().transform(3857)
    heb_geojson = GeoJSONSerializer().serialize(hebrides, use_natural_keys=True, with_modelname=False, srid=3857)
    template = loader.get_template('geodjango_app/index.html')
    context = RequestContext(request, {
        'heb_geojson': heb_geojson,
    })
    return HttpResponse(template.render(context))



def advert(request):
    if request.method == "POST":
        form = AdvertForm(request.POST)

        if(form.is_valid()):
            print(request.POST['title'])
            message = request.POST['title']

        else:
            message = 'something wrong!'


        return render_to_response('contact/advert.html',
                {'message':message},
            context_instance=RequestContext(request))

    else:
        return render_to_response('contact/advert.html',
                {'form':AdvertForm()},
            context_instance=RequestContext(request))