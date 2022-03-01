from django.db import models
from django_quill.fields import QuillField
from django.urls import reverse



# Create your models here.
class KidsContentType(models.Model):
    content_type_id=models.AutoField(primary_key=True)
    content_type_name=models.CharField(max_length=100,blank=False,null=False)

class Content(models.Model):
    content_id=models.AutoField(primary_key=True)
    content_thumbnail=models.ImageField(upload_to="kidstore/image/thumbnail")
    content_cover=models.ImageField(upload_to="kidstore/images/cover")
    content_type=models.ForeignKey(KidsContentType,on_delete=models.CASCADE)
    content_title=models.CharField(max_length=100,blank=False,null=False)
    content_content=QuillField()
    extra_info=models.TextField(blank=True,null=True)
    published=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("kidstore:content-details", kwargs={"content_id": self.content_id})
    

class StoreCatagory(models.Model):
    store_cat_id=models.AutoField(primary_key=True)
    cat_name=models.CharField(max_length=100,blank=False,null=False)

Embed_CHOICES=(("url-embed","URL-Embed"),("html-embed","HTML-Embed"))


class AffilatedProducts(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_cat=models.ForeignKey(StoreCatagory,on_delete=models.CASCADE)
    product_embed_type=models.CharField(max_length=100 ,null=False,blank=False,choices=Embed_CHOICES)
    product_url=models.URLField(null=True,blank=True)
    product_embeded_code=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
