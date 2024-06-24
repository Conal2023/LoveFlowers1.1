from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('title', 'submitted_by', 'location', 'created_at')
    search_fields = ('title', 'submitted_by', 'location', 'content')
    list_filter = ('created_at',)


admin.site.register(Testimonial, TestimonialAdmin)
