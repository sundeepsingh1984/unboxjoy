from enum import Flag
from django.db import models
from sqlalchemy import null
from django_quill.fields import QuillField
from django.urls import reverse

# Create your models here.
class BlogCatagory(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=50,null=False,blank=False)

class BlogSubCategory(models.Model):
    sub_cat_id=models.AutoField(primary_key=True)
    cat_id=models.ForeignKey(BlogCatagory,on_delete=models.CASCADE)
    sub_cat_name=models.CharField(max_length=200)


    

class Blog(models.Model):
    blog_id=models.AutoField(primary_key=True)
    blog_category=models.ForeignKey(BlogCatagory,on_delete=models.CASCADE)
    blog_sub_cat=models.ForeignKey(BlogSubCategory,on_delete=models.CASCADE)
    blog_title=models.CharField(max_length=200,null=False,blank=False)
    blog_content=QuillField()
    blog_cover_img=models.ImageField(upload_to='blogs/images/cover',null=False,blank=False)
    background_img=models.ImageField(upload_to='blogs/images',null=False,blank=False)
    trending=models.BooleanField(default=True)
    public=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("blogs:blog-details", kwargs={"id": self.blog_id})
    
  




