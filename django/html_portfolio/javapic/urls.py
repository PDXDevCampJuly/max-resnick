from django.conf.urls import url
from javapic import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'html_portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.javapic, name='javapichome'),

]
