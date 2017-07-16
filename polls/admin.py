from django.contrib import admin
from .models import Question, Choice

# Register the polls site
admin.site.register(Question)
admin.site.register(Choice)
