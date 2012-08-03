from django.conf.urls.defaults import *
from core import views

urlpatterns = patterns('core.views',
    ('^new/$', 'new_post'),
    ('^$', 'list_posts'),
    #url(r'^$', 'index'),
    #url(r'^(?P<poll_id>\d+)/$', 'detail'),
    #url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)


