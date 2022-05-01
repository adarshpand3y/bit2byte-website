from rest_framework.response import Response
from rest_framework.decorators import api_view

from b2bapp.models import BlogPost, TeamMember
from .serializers import BlogPostSerializer, TeamMemberSerializer

@api_view(["GET"])
def getBlogs(request):
    print("called")
    blogs = BlogPost.objects.all()
    serializedBlogs = BlogPostSerializer(blogs, many=True)
    return Response(serializedBlogs.data)

@api_view(["GET"])
def getParticularBlog(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    serializedBlog = BlogPostSerializer(blog)
    return Response(serializedBlog.data)

@api_view(["GET"])
def getHomeDetails(request):
    teamMembers = TeamMember.objects.all()
    serializedTeamMembers = TeamMemberSerializer(teamMembers, many=True)
    blogs = BlogPost.objects.all()[:5]
    serializedBlogs = BlogPostSerializer(blogs, many=True)
    return Response({"teamMembers": serializedTeamMembers.data, "blogs": serializedBlogs.data})