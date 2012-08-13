from django.conf.urls.defaults import *
from blog import views

urlpatterns = patterns('blog.views', 
    (r'^new/$', 'new_post'),
    (r'^(?P<post_url>[-\w]+)/$', 'display_post'),
    (r'^(?P<post_url>[-\w]+)/edit/$', 'edit_post'),
    (r'^(?P<post_url>[-\w]+)/delete/$', 'delete_post'),
    (r'^$', 'list_posts'),
)