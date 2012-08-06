from django.conf.urls.defaults import *
from blog import views

urlpatterns = patterns('blog.views', 
    url(r'^$', 'list_posts'),
    url(r'^(?P<post_url>[-\w]+)/$', 'display_post'),
    url(r'^new/$', 'new_post'),
)

"""
from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from blog.models import Post

urlpatterns = patterns('blog.views',
    url(r'^$',
        ListView.as_view(
            queryset=Post.objects.order_by('-pub_date')[:5],
            context_object_name ='latest_poll_list', 
            template_name='blog/list_posts.html')), 
            
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Post, 
            template_name='blog/list_posts.html')), 
            
    (r'^new/$', 'new_post'),
    (r'^$', 'list_posts'),
)
"""