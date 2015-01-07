from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'poem_maker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'poem_maker.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('poem_gen.urls', namespace = 'poem_gen'))
)
urlpatterns += staticfiles_urlpatterns()