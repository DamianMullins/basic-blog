from django.conf.urls.defaults import *
from blog import views

urlpatterns = patterns('blog.views', 
    url(r'^new/$', 'new_post'),
    url(r'^(?P<post_url>[-\w]+)/$', 'display_post'),
    url(r'^(?P<post_url>[-\w]+)/edit/$', 'edit_post'),
    url(r'^$', 'list_posts'),
)