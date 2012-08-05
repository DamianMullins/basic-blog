from models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('created_by',)

    def save(self, user, commit = True):
        post = super(PostForm, self).save(commit = False)
        post.created_by = user

        if commit:
            post.save()

        return post