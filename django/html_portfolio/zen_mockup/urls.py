from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.zen_mockup, name='zen_mockup'),
]
