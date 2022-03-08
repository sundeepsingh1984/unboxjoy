from django.db import models
from django.urls import reverse
from django_quill.fields import QuillField
from sqlalchemy import null
from django.core.validators import RegexValidator


class General(models.Model):
    site_name=models.CharField(max_length=200,blank=False,null=False, unique=True)
    site_logo=models.ImageField(upload_to="sites/images")
    bottom_logo=models.ImageField(upload_to="site/images")
    favicon=models.ImageField(upload_to="site/images")
    meta_tag_keywords=models.CharField(max_length=512,null=True,blank=True)
    meta_tag_discription=models.TextField(max_length=200,null=True,blank=True)
    analytics_tag=models.TextField(blank=True,null=True)
    adsense_code=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.site_name}({self.id})'

    


class Banner(models.Model):
    banner_id=models.AutoField(primary_key=True)
    banner_name=models.CharField(max_length=200,null=False,blank=False, unique=True)
    activate=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f'{self.banner_name}({self.banner_id})'





class BannerImages(models.Model):
    image_id=models.AutoField(primary_key=True)
    bannner_id=models.ForeignKey(Banner,on_delete=models.CASCADE)
    banner_image=models.ImageField(upload_to="site/banners")
    image_ref_link=models.URLField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f'{self.banner_image.url}({self.image_id})'










class SocialMediaLinks(models.Model):
    platform_name=models.CharField(max_length=100,null=False,blank=False)
    url=models.URLField(max_length=100)
    icon=models.ImageField(upload_to="site/images" ,null=True)
    
    def __str__(self):
        return f'{self.platform_name}({self.id})'

    

class BusinessInfo(models.Model):
    business_address=QuillField()
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    email=models.EmailField(null=False,blank=False)

    
    def __str__(self):
        return f'{self.phoneNumber}{self.business_address.html} {self.phoneNumber}'


    



class NewsletterSubscribers(models.Model):
    subscriber_id=models.AutoField(primary_key=True)
    email_id=models.EmailField(unique=True,blank=False,null=False)
    
    def __str__(self):
        return f'{self.email_id}({self.subscriber_id})'



class ImportantLink(models.Model):
    link_name=models.CharField(max_length=100,unique=True)
    content=QuillField()
    def get_absolute_url(self):
        return reverse("site-info", kwargs={"id": self.id})

    
    def __str__(self):
        return f'{self.link_name}({self.id})'

    


class CustomAdvertisement(models.Model):
    image=models.ImageField(upload_to="site/ads/images" ,null=True)
    active=models.BooleanField(default=True,blank=False,null=False)
    target_link=models.URLField(blank=False,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.image.value}({self.id})'




# Model for SocialMediaFeed Type
class SocialMediaFeedType(models.Model):
    feed_type_id = models.AutoField(primary_key=True)
    feed_type_name = models.CharField(max_length=100,blank=True,null=True)

    
    def __str__(self):
        return f'{self.feed_type_name}({self.feed_type_id})'


class Feeds(models.Model):
    feed_id=models.AutoField(primary_key=True)
    feed_type=models.ForeignKey(SocialMediaFeedType,on_delete=models.CASCADE)
    feed_code=models.TextField(blank=False,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f'{self.feed_type.feed_type_name} {self.feed_code}'



    

class ContactRequest(models.Model):
    req_id=models.AutoField(primary_key=True)
    email=models.EmailField(blank=False,null=False)
    subject=models.CharField(max_length=100,blank=False,null=False)
    message=models.TextField(blank=False,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

