from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.javapic, name='javapichome'),
    url(r'^join', views.join_javapic, name='join_javapic'),
    url(r'^gallery', views.gallery_javapic, name='gallery_javapic'),
]
