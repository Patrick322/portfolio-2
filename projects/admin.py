from django.contrib import admin
from .models import projects,description
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('description',)

admin.site.register(projects)
admin.site.register(description)  