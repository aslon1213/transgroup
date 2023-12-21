from django.db import models

# Create your models here.


class ContentItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    path = models.CharField(max_length=100)
    LinkToTheDatabase = models.CharField(max_length=100)
    file_itself = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



platforms = (
    ("Telegram", "Telegram"),
    ("Facebook", "Facebook"),
    ("Instagram", "Instagram"),
)


class Comment(models.Model):
    text = models.TextField()
    person= models.CharField(max_length=100)
    person_image = models.ImageField(upload_to='uploads/web_contents/person_images/')
    on_what_platform = models.CharField(max_length=100, choices=platforms, default="Telegram", blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




