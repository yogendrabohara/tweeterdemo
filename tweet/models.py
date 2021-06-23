from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from cloudinary.models import CloudinaryField

# fs = FileSystemStorage(location='./djangopro/tweetdemo/media/photos')

# Create your models here.


class Tweet(models.Model):
    parent_tweet_id = models.IntegerField(default=None, null=True, blank=True)
    name = models.CharField(max_length=180)
    text = models.CharField(max_length=500)
    image = CloudinaryField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    # @property
    # def image_url(self):
    #     if self.image and hasattr(self.image, 'url'):
    #         return self.image.url
