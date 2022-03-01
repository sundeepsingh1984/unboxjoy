"""openjoy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from sitesetting.views import index_view

urlpatterns = [
    path('',index_view,name="index"),
    path('games/',include("games.urls" ,namespace="games")),
    path('giveaway/',include("giveaways.urls",namespace="giveaway")),
    path('admin/', admin.site.urls),
    path('blogs/',include("blogs.urls",namespace="blogs")),
    path('kidzone/',include("kidstore.urls",namespace="kidstore"))
]

#static for games
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
