from django.db import models
from django_summernote.fields import SummernoteTextField


class Testimonial(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = SummernoteTextField()
    submitted_by = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
