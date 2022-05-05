from rest_framework.response import Response
from rest_framework.decorators import api_view

from b2bapp.models import BlogPost, TeamMember, EmailSubscription
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

@api_view(["POST"])
def subscribeToEmail(request, emailId):
    try:
        oldSubsExists = EmailSubscription.objects.filter(email=emailId).exists()
        if not oldSubsExists:
            subscription = EmailSubscription(email=emailId)
            subscription.save()
            return Response({"success": "Subscribed successfully!"})
        else:
            return Response({"error": "That email is already subscribed!"})
    except Exception as e:
        print(e)
        return Response({"error": "Some error ocurred in the subscription process!"})

@api_view(["POST"])
def unsubscribeToEmail(request, emailId):
    try:
        oldSubsExists = EmailSubscription.objects.filter(email=emailId).exists()
        if oldSubsExists:
            subscription = EmailSubscription.objects.get(email=emailId)
            subscription.delete()
            return Response({"success": "Unsubscribed successfully!"})
        else:
            return Response({"error": "That email has not subscribed!"})
    except Exception as e:
        print(e)
        return Response({"error": "Some error ocurred in the unsubscription process!"})