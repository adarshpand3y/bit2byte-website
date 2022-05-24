from django.db import models
from django.utils.text import slugify

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=256, help_text=('Write the title within 200 characters.'))
    metadesc = models.CharField(max_length=512, help_text='Write a desctiprion of this blog in a few sentences')
    body = models.TextField(help_text=('Your main content goes here.'))
    views = models.IntegerField(default=0, help_text=('This statistic is for your reference, do not change it.'))
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=10, choices=[("NEWS", 'News'), ("BLOG", 'Blog')], default="BLOG")
    privacy = models.CharField(max_length=10, choices=[("PRIVATE", 'Private'), ("PUBLIC", 'Public')], default="PRIVATE", help_text=('Public posts will appear to everyone and private posts only to you. Change this to private instead of deleting a post.'))
    slug = models.SlugField(max_length=256, blank=True, help_text=('Leave this parameter empty, it will get generated automatically.'))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    facebookLink = models.CharField(max_length=200, null=True, blank=True)
    instagramLink = models.CharField(max_length=200, null=True, blank=True)
    twitterLink = models.CharField(max_length=200, null=True, blank=True)
    youtubeLink = models.CharField(max_length=200, null=True, blank=True)
    githubLink = models.CharField(max_length=200, null=True, blank=True)
    linkedinLink = models.CharField(max_length=200, null=True, blank=True)
    imageUrl = models.CharField(max_length=200)
    index = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

class EmailSubscription(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email