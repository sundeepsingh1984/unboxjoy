from email import message
from locale import format_string
from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import *
from django.utils.html import format_html
from django.urls import reverse
from django.db import IntegrityError
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.contrib import messages

class WinnersAdmin(admin.ModelAdmin):
    list_display=("id","giveaway","winner")
    
    list_filter=[("giveaway__giveaway_title",DropdownFilter),"created_at"]
    search_fields = ("giveaway__giveaway_title__startswith","winner__name__startswith","winner__email_id__exact","winner__country__startswith","winner__phone_number__exact")


admin.site.register(Winners,WinnersAdmin)








class PlayerAdmin(admin.ModelAdmin):
    list_display=("name","email_id","phone_number","Giveaway_participations","Wins" )
    list_filter=[("country",DropdownFilter),"created_at"]
    search_fields = ("name__startswith","email_id__exact","country__startswith","phone_number__exact")

    def Giveaway_participations (self,obj):
        
        count=obj.giveawayregistration_set.count()
        
        url = (
            reverse("admin:giveaways_giveawayregistration_changelist")
            + "?player="
            + str(obj.id)
        )   
        

        return format_html('<a href="{}"> {} related giveaways</a>', url,count)

    def Wins(self,obj):
        count = obj.winners_set.count()
        url = (
            reverse("admin:giveaways_winners_changelist")
            + "?"
            +"winner=" +str(obj.id)
        )
        
        return format_html('<a href="{}">{} Wins</a>', url, count)
        



admin.site.register(Player,PlayerAdmin)






class GiveawayCategoryAdmin(admin.ModelAdmin):
    list_display=("gawy_cat_id","cat_name","Related_Giveaways" )
    list_filter=["created_at"]
    search_fields = ("catname__startswith",)

    def Related_Giveaways (self,obj):
        
        count=obj.giveaway_set.count()
        
        url = (
            reverse("admin:giveaways_giveaway_changelist")
            + "?giveaway_cat="
            + str(obj.gawy_cat_id)
        )   
        

        return format_html('<a href="{}"> {} related giveaways</a>', url,count)


admin.site.register(GiveawayCategory,GiveawayCategoryAdmin)














#giveaway_registration
class GiveawayRegistrationAdmin(admin.ModelAdmin):
    
    def announce_as_winner(self,request,queryset):
        try:
            for obj in queryset:
                winner_count=obj.giveaway.winners_set.count()
                totalwinner_announced=obj.giveaway.total_winners
                
                if int(totalwinner_announced) > int(winner_count):
                    winner_obj=Winners(giveaway=obj.giveaway,winner=obj.player)
                    winner_obj.save()
                    queryset.update(winner="True")
           

                else:
                    message_string="{} cannot be added as winner ".format(obj.player.name) 
                    self.message_user(request,message_string ,messages.ERROR)


                
            self.message_user(request,"winners announced succesfully" , messages.SUCCESS)


        except IntegrityError  as e:
        
                self.message_user(request,"winners already announced" , messages.WARNING)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))







            







    def remove_as_winner(self,request,queryset):
        try:
            for obj in queryset:
                winner_obj=Winners.objects.filter(giveaway=obj.giveaway,winner=obj.player).get()
                winner_obj.delete()
            
            queryset.update(winner="False")
            self.message_user(request,"Winner removed Success" , messages.SUCCESS)


        except Exception as e:   
            raise e
            self.message_user(request,"OOP's!There was some error performing the action" , messages.ERROR)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))






    
    exclude=("winner",)
    list_display=("reg_id","Player","Giveaway","winner","Previous_Wins")
    list_filter=[("giveaway__giveaway_title",DropdownFilter),"created_at"]
    actions=[remove_as_winner,announce_as_winner]
    search_fields = ("giveaway__giveaway_title__startswith",)


    def Player(self,obj):
        url = (
            reverse("admin:giveaways_player_changelist")
            +"?player_id="
            + str(obj.player.player_id)
        )   

        return format_html('<a href="{}"> {}</a>', url,obj.player.name)

    
    def Giveaway(self,obj):
        url = (
            reverse("admin:giveaways_giveaway_changelist")
            + "?giveaway_id="
            + str(obj.giveaway.giveaway_id)
        )   
        

        return format_html('<a href="{}"> {}</a>', url,obj.giveaway.giveaway_title)

    
    def Previous_Wins(self,obj):
        count = obj.player.winners_set.count()
        url = (
            reverse("admin:giveaways_winners_changelist")
            + "?"
            +"winner=" +str(obj.player)
        )
        
        return format_html('<a href="{}">{} Wins</a>', url, count)
        



admin.site.register(GiveawayRegistration,GiveawayRegistrationAdmin)


#giveaway model

@admin.register(Giveaway)
class QuillPostAdmin(admin.ModelAdmin):
    list_display=("giveaway_title","category","last_apply_date","result_announced","applications")
    list_filter=["created_at","giveaway_cat__cat_name","result_announced"]
    search_fields = ("giveaway_title__startswith",)


    def category(self,obj):
        url = (
            reverse("admin:games_games_changelist")
            + f"{obj.giveaway_cat.gawy_cat_id}"
        )   

        return format_html('<a href="{}"> {}</a>', url,obj.giveaway_cat.cat_name)


    def applications(self, obj):
        count = obj.giveawayregistration_set.count()
        url = (
            reverse("admin:giveaways_giveawayregistration_changelist")
            + "?"
            +"giveaway=" +str(obj.giveaway_id)
        )
        print(url)
        return format_html('<a href="{}">{} Registrations</a>', url, count)
        
        
    applications.short_description = "Registrations"






