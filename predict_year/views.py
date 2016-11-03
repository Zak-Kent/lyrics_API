from django.shortcuts import render

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404

from rest_framework.exceptions import ParseError

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

    song_lyrics = request.body

    # Check request body to make sure it's 4 words or longer 
    text_list = song_lyrics.split()
    if len(text_list) < 4:
        detail = "your request body must be longer than three words"
        raise ParseError(detail=detail, code=400) 

    # check to make sure body doesn't contain numbers 
    int_in_text = [word.isdigit() for word in text_list]
    for item in int_in_text: 
        if item: 
            detail = "your request must not contain numbers"
            print(detail)
            raise ParseError(detail=detail, code=400) 

    # send data to predict.py for stemming, dict conversion, and prediction
    parse_data_predict(song_lyrics)

    # grabs most recently created object from DB so you can access prediction 
    obj = Song_BOW.objects.all().order_by('-id')[0]

    # turns object into python dict so you can access it 
    serializer = BOWSerializer(obj)
    print(serializer.data)

    json = JSONRenderer().render(serializer.data)

    return HttpResponse(json)

    # except:
    #     print(Exception)
    #     raise Http404("failure in processing your string")



