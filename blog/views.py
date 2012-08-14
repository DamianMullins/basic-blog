from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import PostForm
from models import Post

@login_required
def new_post(request):
    "Add a new post"
    form = PostForm()
    button_text = 'Insert'
    instructions_template = 'blog/includes/insert_post_instructions.html'
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('blog.views.display_post', 
                                        args=(request.REQUEST["url"],)))
            
    return render_to_response('blog/edit_form.html', 
                              locals(), 
                              context_instance=RequestContext(request))


@login_required
def edit_post(request, post_url):
    "Edit an existing post"
    post = get_object_or_404(Post, url=post_url)
    form = PostForm(instance=post)
    button_text = 'Update'
    instructions_template = 'blog/includes/edit_post_instructions.html'
		
    if request.method == 'POST':
        post = get_object_or_404(Post, url=post_url)
        form = PostForm(request.POST, instance=post)
				
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('blog.views.display_post', 
                                        args=(post.url,)))
																				
    return render_to_response('blog/edit_form.html', 
                              locals(), 
                              context_instance=RequestContext(request))


@login_required
def delete_post(request, post_url):
    "Delete an existing post"
    post = get_object_or_404(Post, url=post_url)
    form = PostForm(instance=post)

    if request.method == 'POST':
        post = get_object_or_404(Post, url=post_url)
        form = PostForm(request.POST, instance=post)

        post.delete()
        return HttpResponseRedirect(reverse('blog.views.list_posts'))

    return render_to_response('blog/delete_post.html', 
                              locals(), 
                              context_instance=RequestContext(request))


def list_posts(request):
    "List all active posts with a publish date in the past"
    posts = Post.objects.filter(pub_date__lte=datetime.now()).order_by('-pub_date')
    
    return render_to_response('blog/list_posts.html', 
                              locals(), 
                              context_instance=RequestContext(request))


def display_post(request, post_url):
    "Display a single post"
    post = get_object_or_404(Post, url=post_url)
    
    return render_to_response('blog/display_post.html', 
                              locals(), 
                              context_instance=RequestContext(request))