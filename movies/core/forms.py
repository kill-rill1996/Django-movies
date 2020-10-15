from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Forms for review"""
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')
