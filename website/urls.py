from django.conf.urls import patterns, include, url
import website.views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'temponaryWebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'website.views.index', name='index'),
    url(r'^view/(?P<hash>.+)$', website.views.viewSite, name='viewSite'),
)