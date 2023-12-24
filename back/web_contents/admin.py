from django.contrib import admin
from .models import ContentItem, Comment, EmailToBeContacted
# Register your models here.
# from .models import ContentItem, Comment
admin.site.register(ContentItem)
admin.site.register(Comment)
admin.site.register(EmailToBeContacted)


