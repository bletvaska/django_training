from django.contrib import admin
from django import forms
from pyper.models import Post, Tag

class FormPost( forms.ModelForm ):
    content = forms.CharField( widget=forms.Textarea )

class AdminPost(admin.ModelAdmin):
    fields = ['content', 'author']
    form = FormPost

    # def save_model(self, request, obj, form, change):
        # obj.save()


# Register your models here.
admin.site.register(Post, AdminPost)
admin.site.register(Tag)
