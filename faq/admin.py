from django.contrib import admin
from .models import FAQ, Post
from django_summernote.admin import SummernoteModelAdmin


class FAQAdmin(SummernoteModelAdmin):  
    summernote_fields = ('answer',)


class PostAdmin(SummernoteModelAdmin):  
    summernote_fields = ('content',)


admin.site.register(FAQ, FAQAdmin)
admin.site.register(Post, PostAdmin)
