from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'html_portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^javapic/', include('javapic.urls')),
    url(r'^javapic_jquery', include('javapic_jquery.urls'))
]
