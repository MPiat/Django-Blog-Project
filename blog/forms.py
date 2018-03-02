from django import forms
from blog.models import BlogPost, Comment
#from django.forms.widgets import TextArea

class BlogPostForm(forms.ModelForm):

    class Meta():
        model = BlogPost
        fields = ('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.Textarea(attrs = {'class':'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.Textarea(attrs = {'class':'editable medium-editor-textarea'}),
        }
