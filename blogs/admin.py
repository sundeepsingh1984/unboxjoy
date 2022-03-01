from audioop import reverse
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Blog,BlogSubCategory,BlogCatagory

class BlogCatagoryAdmin(admin.ModelAdmin):
    list_display=("category_name",)
    search_fields = ("category_name__startswith",)


class BlogSubCategoryAdmin(admin.ModelAdmin):
    list_display=("sub_cat_name","related_category",)
    search_fields = (" sub_cat_name__startswith",)
    list_filter=("cat_id__category_name",)
    
    def related_category(self,obj):
        url=(reverse("admin:blogs_blogsubcategory_changelist") + f"{obj.cat_id.category_id}")
        return format_html('<a href="{}"> {}</a>', url,obj.cat_id.category_name)

admin.site.register(BlogCatagory,BlogCatagoryAdmin)
admin.site.register(BlogSubCategory,BlogSubCategoryAdmin)

@admin.register(Blog)
class QuillPostAdmin(admin.ModelAdmin):

    #custom actions

    def publish_blog(modeladmin, request, queryset):
        queryset.update(public = "True")

    def unpublish_blog(modeladmin, request, queryset):
        queryset.update(public = "False")
     
   
   
   
   
   
   
    list_display=("blog_title","public","trending" ,"category","subcategory")
    list_filter=["trending","public","blog_category__category_name","blog_sub_cat__sub_cat_name","created_at"]
    search_fields = ("blog_title__startswith",)
    actions=[publish_blog,unpublish_blog]



    def category(self,obj):
        url=(reverse("admin:blogs_blogcatagory_changelist") + f"{obj.blog_category.category_id}")
        return format_html('<a href="{}"> {}</a>', url,obj.blog_category.category_name)

    
    def subcategory(self,obj):
        url=(reverse("admin:blogs_blogsubcategory_changelist") + f"{obj.blog_sub_cat.sub_cat_id}")
        return format_html('<a href="{}"> {}</a>', url,obj.blog_sub_cat.sub_cat_name)
        
