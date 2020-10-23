from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from . models import Images
from . serializers import ImageSerializer

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image


data = '<html><body><h1>리턴입니다.</h1></body></html>'


@csrf_exempt
def image_send(request):
    if request.method == 'GET':
        queryset = Images.objects.all()
        serializer = ImageSerializer(queryset, many=True)
        # return HttpResponse(data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        img_model = Images()
        try:
            # 여기서 file을 튜플 형태로 client가 보낸 그대로 받아옮.
            file = request.FILES.popitem()
            # file = file[0]
            # print("여기까지는 됨")
            # print(file)
            # print("file의 타입은:", type(file))
            # print(file[1])
            # print("file[1]의 타입은:", type(file[1]))
            file = file[1][0].file
            img = Image.open(file)
            img.save('newfile.jpg')
            # path = default_storage.save(
            #     '../upload_test/test.jpg', ContentFile(file[1]))
            # print(path + "저장 완료")
            print("성공")
            return HttpResponse("file received")
        except:
            print("No Post")
            return HttpResponse("No Post")
