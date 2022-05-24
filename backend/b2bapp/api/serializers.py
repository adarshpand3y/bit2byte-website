from rest_framework import serializers

from b2bapp.models import BlogPost, TeamMember

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'metadesc', 'body', 'views', 'publish_date', 'last_updated', 'category', 'slug']

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = "__all__"