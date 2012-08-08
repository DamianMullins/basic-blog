from models import Post
from django import forms
from django.template.defaultfilters import slugify

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'url', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'short'}),
            'url': forms.TextInput(attrs={'class': 'short'}),
            'content': forms.Textarea(attrs={'rows': 15}),
        }

    def save(self, user, commit = True):
        post = super(PostForm, self).save(commit = False)
        post.url = slugify(post.url)
        post.created_by = user

        if commit:
            post.save()

        return post
        
        
    """
    def clean_url(self):
        "Check that submitted URL is unique and allowed"
        INVALID_URLS = ('about', 'admin', 'register')    
        url = self.cleaned_data['url']
        
        try:
            post = Post.objects.get(url=url)
        except Post.DoesNotExist:
            pass
        else:
            raise forms.ValidationError(u'%s already exists' % post )
    
        if url in INVALID_URLS:
            raise forms.ValidationError(u'%s is not a valid url' % url )
    
        return url
    """