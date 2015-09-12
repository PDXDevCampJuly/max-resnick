from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'html_portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.forum, name='forum'),

]
