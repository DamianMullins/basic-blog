from datetime import datetime
from django.template import Library, Node
from blog.models import Post

register = Library()

@register.inclusion_tag('blog/templatetags/latest_posts.html')
def latest_posts(number_of_posts):
    posts = Post.objects.filter(pub_date__lte=datetime.now()).order_by('-pub_date')[:number_of_posts]

    return {'posts':posts}