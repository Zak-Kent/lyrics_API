from django.shortcuts import render

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer

from models import Song_BOW
from predict_year.serializers import BOWSerializer

from predict import parse_data_predict

@csrf_exempt
@api_view(['POST'])
def parse_data(request):
    """ Request comes into API via POST, song lyrics in a 'payload' object, 
        take lyrics and transform them into number counts, tfidf scores, and pass
        to NB model. Write prediction to lyrics object's year attribute and return 
        year prediction  
    """

    # try:
    info = request.body
    print("inside view: {}".format(info))
    # info = request.POST.get('payload', 'no info')
    # print("data inside post request: {}".format(info))

    # calls parse data func to create obj with text
    parse_data_predict(info)

    # grabs most recently created object so you can access values 
    obj = Song_BOW.objects.all().order_by('-id')[0]
    # print(obj.bow)
    # prin)t(obj.year)

    # turns object into python dict so you can access it 
    serializer = BOWSerializer(obj)
    print('I dond know')
    print(serializer.data)

    json = JSONRenderer().render(serializer.data)

    return HttpResponse(json)

    # except Exception:
    #     print(Exception)
    #     # logger.exception('New way')
    #     # return render(request, 'home.html')

    #     print('failed in parse_data view')
    #     return HttpResponse("fail in http response")



