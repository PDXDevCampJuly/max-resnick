from django.conf.urls import url
from javapic import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'html_portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.javapic, name='javapichome'),
    url(r'^join', views.join_javapic, name='join_javapic'),
    url(r'^gallery', views.gallery_javapic, name='gallery_javapic'),

]
