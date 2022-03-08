from django.contrib import admin
from .models import *
from django.utils.html import format_html

#customize general model

class GeneralAdmin(admin.ModelAdmin):
    list_display=("site_name","site_logo","bottom_logo","favicon")
    search_fields = ("site_name__startswith",)

# register general model
admin.site.register(General,GeneralAdmin)




class BannerAdmin(admin.ModelAdmin):
    list_display=("banner_name","Images")
    search_fields = ("banner_name__startswith",)
    list_filter=["created_at"]

    def Images(self,obj):
        count=obj.bannerimages_set.count()
        
        url = (
            reverse("admin:sitesetting_bannerimages_changelist")
            + "?"
            +"bannner_id=" +str(obj.banner_id)
            )   
        

        return format_html('<a href="{}"> {} related Images</a>', url,count)


# register general model
admin.site.register(Banner,BannerAdmin)




class BannerImagesAdmin(admin.ModelAdmin):
    list_display=("image_id","bannner_id","banner_image","image_ref_link")
    search_fields = ("bannner_id__banner_name__startswith",)
    

# register general model
admin.site.register(BannerImages,BannerImagesAdmin)


class SocialMediaLinksAdmin(admin.ModelAdmin):
    list_display=("platform_name","url","icon",)
    search_fields = ("platform_name__startswith",)
   
# register general model
admin.site.register(SocialMediaLinks,SocialMediaLinksAdmin)


class BusinessInfoAdmin(admin.ModelAdmin):
    list_display=("Address","phoneNumber","email")
    

    def Address(self,obj):
        return format_html('<div> {} </div>',obj.business_address.html)


   
# register general model
admin.site.register(BusinessInfo,BusinessInfoAdmin)




class NewsletterSubscribersAdmin(admin.ModelAdmin):
    list_display=("subscriber_id","email_id")
    
# register general model
admin.site.register(NewsletterSubscribers,NewsletterSubscribersAdmin)



class ImportantLinksAdmin(admin.ModelAdmin):
    list_display=("link_name",)

    
    
# register general model
admin.site.register(ImportantLink,ImportantLinksAdmin)
    

class CustomAdvertisementAdmin(admin.ModelAdmin):
    list_display=("image","active","target_link",)

admin.site.register(CustomAdvertisement,CustomAdvertisementAdmin)


class SocialMediaFeedTypeAdmin(admin.ModelAdmin):
    list_display=("feed_type_id","feed_type_name","Feeds")


    def Feeds(self,obj):
        count=obj.feeds_set.count()
        
        url = (
            reverse("admin:sitesetting_feeds_changelist")
            + "?"
            +"feed_type=" + str(obj.feed_type_id)
            )   
        

        return format_html('<a href="{}"> {} related Feeds</a>', url,count)





class FeedsAdmin(admin.ModelAdmin):
    list_display=("feed_id","feed_type",)
    search_fields = ("feed_type__feed_type_name__startswith",)
    list_filter=["created_at"]



admin.site.register(Feeds,FeedsAdmin)




class ContactRequestAdmin(admin.ModelAdmin):
    list_display=("req_id","email","subject","message")
    search_fields = ("email__startswith","req_id__startswith")
    list_filter=["created_at"]


admin.site.register(ContactRequest,ContactRequestAdmin)


admin.site.register(SocialMediaFeedType,SocialMediaFeedTypeAdmin)