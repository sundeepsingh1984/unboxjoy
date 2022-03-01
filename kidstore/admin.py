from django.contrib import admin
from .models import *
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.utils.html import format_html
from django.contrib import messages

#register quill models
@admin.register(Content)
class QuillPostAdmin(admin.ModelAdmin):
        #custom actions

    def publish_blog(self, request, queryset):
        self.message_user(request,"Content Published Succesfully" , messages.SUCCESS)
        queryset.update(published = "True")

    def unpublish_blog(self, request, queryset):
        self.message_user(request,"Content UnPublished Succesfully" , messages.SUCCESS)
        queryset.update(published = "False")
     
   
    list_display=("content_id","content_title","published","Content_type")
    list_filter=["published",("content_type__content_type_name",DropdownFilter),"created_at",]
    search_fields = ("content_title__startswith",)
    actions=[publish_blog,unpublish_blog]



    def Content_type(self,obj):
        url = (
            reverse("admin:kidstore_kidscontenttype_changelist")
            + "?content_type_id="
            + str(obj.content_type.content_type_id)
        )   
        

        return format_html('<a href="{}"> {} </a>', url,obj.content_type.content_type_name)


#customization of KidsContentType model
class KidsContentTypeAdmin(admin.ModelAdmin):
    list_display=("content_type_id","content_type_name","Content")
    search_fields = ("content_type_name__startswith",)
    


    def Content(self,obj):
        
        count=obj.content_set.count()
        
        url = (
            reverse("admin:kidstore_content_changelist")
            + "?content_type="
            + str(obj.content_type_id)
        )   
        

        return format_html('<a href="{}"> {} related content"s </a>', url,count)


 #registerig KidsContentType model

admin.site.register(KidsContentType,KidsContentTypeAdmin)


#customization of StoreCategory model
class StoreCatagoryAdmin(admin.ModelAdmin):
    list_display=("store_cat_id","cat_name","Products")
    search_fields = ("cat_name__startswith",)
    


    def Products(self,obj):
        
        count=obj.affilatedproducts_set.count()
        
        url = (
            reverse("admin:kidstore_affilatedproducts_changelist")
            + "?product_cat="
            + str(obj.store_cat_id)
        )   
        

        return format_html('<a href="{}"> {} related product"s </a>', url,count)



# Register StoreCatagory  models here.

admin.site.register(StoreCatagory,StoreCatagoryAdmin)




#customizing AffilatedProducts

class AffilatedProductsAdmin(admin.ModelAdmin):
        
    list_display=("product_id","Category","product_embed_type")
    list_filter=[("product_cat__cat_name",DropdownFilter),("product_embed_type",DropdownFilter),"created_at",]
    search_fields = ("product_cat__cat_name__startswith",)
    



    def Category(self,obj):
        url = (
            reverse("admin:kidstore_storecatagory_changelist")
            + "?store_cat_id="
            + str(obj.product_cat.store_cat_id)
        )   
        

        return format_html('<a href="{}"> {} </a>', url,obj.product_cat.cat_name)



# Registering  AffilatedProducts models here.
admin.site.register(AffilatedProducts,AffilatedProductsAdmin)





