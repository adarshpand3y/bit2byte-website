from django.contrib import admin
from .models import BlogPost, TeamMember

# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    # class Media:
    #     js = ("tinymce.js",)

    list_display = ('title', 'publish_date', 'privacy', 'views')
    readonly_fields = ['views']

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')