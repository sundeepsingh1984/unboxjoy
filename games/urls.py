from django.urls import path
from . import views
from . import apps

app_name = apps.GamesConfig.name
urlpatterns=[
    path("<int:game_id>/<int:update_type_id>",views.games_content_view,name="game-updates"),
    path("details/<int:update_id>",views.game_update_details_view,name="game-update-details-view")
    ]