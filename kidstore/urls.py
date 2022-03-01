from django.urls import path
from . import views
from . import apps

app_name=apps.KidstoreConfig.name

urlpatterns=[
    path("store",views.kids_store_view ,name="kids-store"),
    path("store/filtered",views.kids_store_refined_view ,name="kids-store-filtered"),
    path("content/<int:category_id>",views.kids_corner_content_view ,name="kids-corner-content-view"),
    path("content/details/<int:content_id>",views.content_detail_view,name="content-details")


    ]