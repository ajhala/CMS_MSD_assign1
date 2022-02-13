from django import forms

from .models import *


class CustomUserCreationForm(CommentForm):
    class Meta(CommentForm):
        model = Comment
        fields = 'comment'
