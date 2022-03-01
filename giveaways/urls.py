from django.urls import path
from . import views
from . import apps

app_name=apps.GiveawaysConfig.name

urlpatterns=[
    path("<int:cat_id>",views.giveaway_catogorical_view ,name="giveaway-by-category"),
    path("details/<int:gawy_id>",views.giveaway_detail_view  ,name="giveaway-detail"),
    path("verify-register",views.verify_and_register_player,name="player-giveaway-verify-register"),
    path("register-player",views.register_player,name='player-registration'),


    ]