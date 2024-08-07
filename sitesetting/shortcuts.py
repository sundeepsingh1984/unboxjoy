
from ast import Pass
from django.http import Http404
from .forms import SubscribeForm
from .models import *
from django.shortcuts import get_object_or_404
from games.models import Games
from blogs.models import BlogCatagory
from giveaways.models import GiveawayCategory
from kidstore.models import KidsContentType
def get_site_info(request):
    """
    returns the site info 
    """

    try:
        info=General.objects.get()
        return info
    except Exception as e:
        Pass
    


def get_games_menu(request):
    """
    returns games model
    """

    try:
        games=Games.objects.all()
        return games

    except Exception as e:
        pass

    
def get_blogs_category(request):
    """
    returns blog category model
    """

    try:
       blog_cat=BlogCatagory.objects.all()
       return blog_cat
        

    except Exception as e:
        raise Http404("Error Fetching Site Details")


def get_giveaway_type(request):
    """
    returns blog category model
    
    """

    try:
        giveaway_cat= GiveawayCategory.objects.all()
        return giveaway_cat

    except Exception as e:
       pass

# return the social links
def get_social(request):
    try:
        links=SocialMediaLinks.objects.all()
        return links
    
    except Exception as e:
        pass


#divide a list into chunk of lists
def divide_chunks(l, n):

    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]



# return banner or default banner
def get_banner_by_name(name):

    try:
        banner=Banner.objects.filter(banner_name__istartswith=name ,activate="True").first()

    except Banner.DoesNotExist as e:
        banner=Banner.objects.filter(activate="True").first()

        


    return banner


def get_kids_content_category(request):

    try:
        kids_content_qset=KidsContentType.objects.all()

        return kids_content_qset

    except Exception as e:

        raise Http404("there is some issue fetching kids content")



def get_business_info(request):
    try:
        business_info=BusinessInfo.objects.first()

        return business_info

    except Exception as e:

        raise Http404("there is some issue fetching kids content")

def get_important_links(request):
    try:
        links=ImportantLink.objects.all()
        return links

    except Exception as e:
        raise Http404("there is some issue fetching kids content")


def get_subscribtion_form(request):

    return SubscribeForm