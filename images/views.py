from django.shortcuts import render
from django.template import Context, loader
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

import datetime
import os


@csrf_exempt
def init(request):
    template = loader.get_template("index.html")
    queryset = Images.objects.all()
    queryset = queryset.order_by('-created')[:8]
    for query in queryset:
        query.caption = query.caption[48:]
    context = {'images': queryset, }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def image_send(request):
    if request.method == 'GET':
        template = loader.get_template("sample.html")
        queryset = Images.objects.all()
        # 8개로 제한 연습(index.html이 8개 정도기에)
        queryset = queryset.order_by('-created')[:8]
        for query in queryset:
            query.caption = query.caption[48:]
            # /Users/Han/programming/restfulapi/images/static/media/{}.jpg 경로에서 media 부터 시작하기 위함으로 슬라이싱
        context = {'images': queryset, }
        # serializer = ImageSerializer(queryset, many=True)
        # return JsonResponse(serializer.data, safe=False)
        # return render(request, '/Users/Han/programming/restfulapi/images/templates/index.html', {'images': queryset, })
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        img_model = Images()
        try:
            # 여기서 file을 튜플 형태로 client가 보낸 그대로 받아옮.
            file = request.FILES.popitem()
            file = file[1][0]
            print(file)
            binary_file = file.file
            print(binary_file)
            img = Image.open(binary_file)
            print(img)
            num = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            # path = '/Users/Han/programming/restfulapi/upload_test/test{}.jpg'.format(
            #     num)
            # print(path)
            # print(type(path))
            abspath = os.path.abspath("./images/static/media/test{}.jpg".format(
                num))
            print(abspath)
            print(type(abspath))
            img.save(
                abspath, 'JPEG')
            serializer = ImageSerializer(
                data={'caption': abspath, 'created': ''})
            if serializer.is_valid():
                print("db 저장 시작")
                serializer.save()
                print("db 저장 성공")
            else:
                print("db 저장 실패")

            print("완전 성공")
            return HttpResponse("file received")
        except:
            print("No Post")
            return HttpResponse("No Post")
