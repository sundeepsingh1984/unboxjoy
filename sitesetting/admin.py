from django.contrib import admin
from .models import *


#register quill models
@admin.register(*[General,ImportantLink,BusinessInfo,CustomAdvertisement])
class QuillPostAdmin(admin.ModelAdmin):
    pass



# Register your models here.
admin.site.register([Banner,BannerImages,SocialMediaLinks,SocialMediaFeedType,Feeds])