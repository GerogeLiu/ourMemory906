from django.contrib import admin
from .models import BlogArticles

# Register your models here.
# admin.site.register(BlogArticles)

@admin.register(BlogArticles)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ["publish", "author"]
