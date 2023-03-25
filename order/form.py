from django import forms
from .models import Orders

class PostForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = [
            'tags']