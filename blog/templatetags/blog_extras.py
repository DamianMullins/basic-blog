from datetime import datetime
from django.template import Library, Node
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from blog.models import Post
import re

register = Library()

@register.inclusion_tag('blog/templatetags/latest_posts.html')
def latest_posts(number_of_posts):
    posts = Post.objects.filter(pub_date__lte=datetime.now()).order_by('-pub_date')[:number_of_posts]

    return {'posts':posts}