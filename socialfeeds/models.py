from django.db import models

# Create your models here.

# Model for Feed Type
class FeedType(models.Model):
    feed_type_id = models.AutoField(primary_key=True)
    feed_type_name = models.CharField(max_length=100,blank=True,null=True)

# Model for Feeds
class Feeds(models.Model):
    feed_id=models.AutoField(primary_key=True)
    feed_type=models.ForeignKey(FeedType,on_delete=models.CASCADE)
    feed_code=models.TextField(blank=False,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
