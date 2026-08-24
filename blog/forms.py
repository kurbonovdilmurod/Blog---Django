from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )

class PostEditForm(forms.ModelForm):
    class  Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'categories']

    title = forms.CharField(widget=forms.TextInput)
    content = forms.CharField(widget=forms.Textarea(attrs={"size": "100"}))
    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)