from atexit import register
import imp
from msilib.schema import Class
from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import Games,GameUpdates,GameUpdateType


admin.site.empty_value_display = '(None)'

admin.site.site_header="UnboxJoy Adminstrator"
admin.site.site_title="Unboxjoy Site Admin"

# Register your models here.

class GamesAdmin(admin.ModelAdmin):
    exclude = ("created_at", "updated_at")
    list_display=("game_name","play_link","game_landing_page_link")
    search_fields = ("game_name__startswith",)
    list_filter=("created_at",)


class GameUpdateTypeAdmin(admin.ModelAdmin):

    list_display=("update_type_name","related_game",)
    search_fields = ("update_type_name__startswith",)

    
    def related_game(self, obj):
        url = (
            reverse("admin:games_games_changelist")
            + f"{obj.game.game_id}"
        )   

        return format_html('<a href="{}"> {}</a>', url,obj.game.game_name)







admin.site.register(Games,GamesAdmin)
admin.site.register(GameUpdateType,GameUpdateTypeAdmin)













@admin.register(GameUpdates,)

class QuillPostAdmin(admin.ModelAdmin):
    exclude = ("created_at", "updated_at")
    list_display=("update_title","update_link","view_game","view_type")
    
    list_filter=("update_for__game_name","update_type__update_type_name","created_at")
    search_fields = ("update_title__startswith","update_description__icontains" )

    def view_game(self, obj):
        url=(reverse('admin:games_games_changelist')
        +f"{obj.update_for.game_id}"
        )
        
        return format_html('<a href="{}"> Related Game</a>', url)


    def view_type(self, obj):
        url = (
            reverse("admin:games_gameupdatetype_changelist")
            + f"{obj.update_type.update_type_id}"
        )
        
        return format_html('<a href="{}"> Related Type</a>', url)

    









