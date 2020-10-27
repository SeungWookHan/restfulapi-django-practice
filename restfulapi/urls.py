"""restfulapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from addresses import views as addressviews
from images import views as imageviews
from django.views.static import serve
from . settings import STATIC_ROOT
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # url(r'^addresses/', views.address_list),
    # url(r'^addresses/', views.address_list),
    path('', imageviews.init),
    path('addresses/', addressviews.address_list),
    path('addresses/<int:pk>/', addressviews.address),
    path('login/', addressviews.login),
    path('api-auth/', include('rest_framework.urls')),
    path('images/', imageviews.image_send),
    # url(r'^static/(?P<path>.*)$', serve,
    #     {'document_root': STATIC_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# redirects to static media files (css, javascript, images, etc.)
# (r'^static/(?P<path>.*)$', 'django.views.static.serve',
#  {'document_root': 'static/'}),
