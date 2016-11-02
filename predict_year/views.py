from django.shortcuts import render
# from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from django.http import HttpResponse

from models import Song_BOW
from predict_year.serializers import BOWSerializer

from predict import parse_data_predict


@api_view(['POST'])
def parse_data(request):
    """ As a request comes from the home page via POST, parse the canvas
    image, downsize it to match the dims of the training data, and then
    pass it to the pre-trained neural network for it make a prediction.
    The results of the prediction (value and confidence), as well as the
    array representations of the images themselves are stored in the
    model, and hence the PostgresQL database.
    """

    try:
        info = request.POST.get('payload', 'no info')
        print("data inside post request: {}".format(info))

        # calls parse data func to create obj with text
        parse_data_predict(info)

        # grabs most recently created object so you can access values 
        obj = Song_BOW.objects.all().order_by('-id')[0]
        print(obj.bow)
        print(obj.year)

        # turns object into python dict so you can access it 
        serializer = BOWSerializer(obj)
        print(serializer.data)
        return HttpResponse(serializer.data)

    except:
        # logger.exception('New way')
        # return render(request, 'home.html')

        print('failed in parse_data view')
        return HttpResponse("test of http response")



