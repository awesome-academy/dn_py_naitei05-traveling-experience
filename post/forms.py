from django import forms

from post.models import Post

class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 
                                                        'id': 'padding-bottom-border',
                                                        'type': 'text', 'name': 'title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 
                                                        'id': 'padding-bottom-border',
                                                        'rows': '5', 'name': 'title'}))
    image = forms.ImageField()
