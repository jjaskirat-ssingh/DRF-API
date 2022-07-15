from rest_framework import serializers
# from django import forms
from .models import Post

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = {
#             'title', 'description'
#         }

# similar as we create PostForm
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'description', 'owner'
        )