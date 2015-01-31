# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from .views import home, home_files #relative import- now the name of project can be changed without breaking the urls
#an absolute import : taskbuster.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'taskbuster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(?P<filename>(robots.txt)|(humans.txt))$', home_files, name='home-files')
)

urlpatterns += i18n_patterns('',
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),


)