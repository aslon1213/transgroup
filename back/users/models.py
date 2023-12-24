from django.db import models

# Create your models here.


class EmailToBeContacted(models.Model):
    email = models.EmailField(max_length=254, unique=True, blank=False, null=False)
    contacted_yet = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email