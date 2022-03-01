from django.urls import path
from . import views
from . import apps
app_name=apps.BlogsConfig.name
urlpatterns=[
    path("",views.blogs_home_view,name="blogs-home"),
    path("blog-detail/<int:id>",views.blog_detail_view,name="blog-details"),
    path("<int:cat_id>",views.blogs_categorical_view,name="blogs-by-category"),
    path("<int:cat_id>/<int:sub_cat_id>",views.blogs_subcategorical_view,name="blogs-by-sub-category"),
    ]