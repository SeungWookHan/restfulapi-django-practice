from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from . models import Images
from . serializers import ImageSerializer


data = '<html><body><h1>리턴입니다.</h1></body></html>'


@csrf_exempt
def image_send(request):
    if request.method == 'GET':
        queryset = Images.objects.all()
        serializer = ImageSerializer(queryset, many=True)
        # return HttpResponse(data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        print(request)
        try:
            file = request.FILES['send']
            file.save("newfile.jpg")
            print(file)
            return HttpResponse("file received")
        except:
            return HttpResponse("No Post")
