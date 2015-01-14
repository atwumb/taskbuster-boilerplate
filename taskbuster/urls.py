from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import home #relative import- now the name of project can be changed without breaking the urls
#an absolute import : taskbuster.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'taskbuster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
)
