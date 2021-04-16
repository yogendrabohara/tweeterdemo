from django import forms
from django.forms import ModelForm, Textarea, TextInput, ClearableFileInput
from .models import Tweet


class NewUserForm(forms.ModelForm):

    class Meta:

        model = Tweet
        # fields = '__all__'
        fields = ['parent_tweet_id' ,'name', 'text', 'image']
        widgets = {
            'name': TextInput(attrs= {'class':'tweet-name', 'placeholder':'Your post name'}),
            'text': Textarea(attrs={'class':'tweet-textarea', 'placeholder':"What’s happenning?", 'rows':7, 'cols':100}),
            'image': ClearableFileInput(attrs= {'class':'tweet-form-image'}),
        }