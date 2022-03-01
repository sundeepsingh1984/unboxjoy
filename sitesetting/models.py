from distutils.command.upload import upload
from pyexpat import model
from turtle import update
from django.db import models
from enum import Enum, unique

from django.forms import CharField
from django_quill.fields import QuillField
from sqlalchemy import null
from django.core.validators import RegexValidator


class General(models.Model):
    site_name=models.CharField(max_length=200,blank=False,null=False)
    site_logo=models.ImageField(upload_to="sites/images")
    bottom_logo=models.ImageField(upload_to="site/images")
    favicon=models.ImageField(upload_to="site/images")
    meta_tag_keywords=models.CharField(max_length=512,null=True,blank=True)
    meta_tag_discription=models.TextField(max_length=200,null=True,blank=True)
    analytics_tag=models.TextField(blank=True,null=True)
    adsense_code=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    


class Banner(models.Model):
    banner_id=models.AutoField(primary_key=True)
    banner_name=models.CharField(max_length=200,null=False,blank=False, unique=True)
    activate=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)




class BannerImages(models.Model):
    image_id=models.AutoField(primary_key=True)
    bannner_id=models.ForeignKey(Banner,on_delete=models.CASCADE)
    banner_image=models.ImageField(upload_to="site/banners")
    image_ref_link=models.URLField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)









class SocialMediaLinks(models.Model):
    platform_name=models.CharField(max_length=100,null=False,blank=False)
    url=models.URLField(max_length=100)
    icon=models.ImageField(upload_to="site/images" ,null=True)
    

class Information(models.Model):
    site_owner=models.CharField(max_length=50)
    business_address=QuillField()
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    email=models.EmailField(null=False,blank=False)



class NewsletterSubscribers(models.Model):
    subscriber_id=models.AutoField(primary_key=True)
    email_id=models.EmailField(unique=True,blank=False,null=False)


class ImportantLink(models.Model):
    Link_name=models.CharField(max_length=100,unique=True)
    content=QuillField()


class CustomAdvertisement(models.Model):
    icon=models.ImageField(upload_to="site/images" ,null=True)
    active=models.BooleanField(default=True,blank=False,null=False)
    target_link=models.URLField(blank=False,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    

