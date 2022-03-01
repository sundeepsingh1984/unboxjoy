import imp
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import GameUpdateType, GameUpdates, Games
from django.http import Http404
from .filters import GameUpdateFilter
from django.core.paginator import Paginator
# Create your views here.

# kids content view
def games_content_view(request,game_id,update_type_id):

    try:
        #query set

        game_obj=Games.objects.filter(game_id=game_id).order_by("-created_at").get()
        updates_qs=game_obj.gameupdates_set.filter(update_type=update_type_id).order_by("-created_at").all()
        categories=game_obj.gameupdatetype_set.exclude(update_type_id = update_type_id).all()
        filtered_qs=GameUpdateFilter(request.GET,updates_qs)
        page_obj=Paginator(filtered_qs.qs,6)
        page_number=request.GET.get("page")
    except Exception as e:
        raise e
        raise Http404("There is Some Error fetching products.Please Try again after a while")
    
    try:
        page_obj = page_obj.get_page(page_number)  # returns the desired page object
        
    except  PageNotAnInteger:
    # if page_number is not an integer then assign the first page
        page_obj = page_obj.page(1)
        
    except EmptyPage:
        # if page is empty then return last page
        page_obj = page_obj.page(page_obj.num_pages)
    
        
    # sending the page object to pages
    return render(request,"games-view.html",{"updates":page_obj,"filter_form":filtered_qs.form,"categories":categories,"game":game_obj})


def game_update_details_view(request,update_id):

    try:

        update_obj=GameUpdates.objects.filter(update_id=update_id).get()
        categories=update_obj.update_for.gameupdatetype_set.all()
        latest_updates=GameUpdates.objects.order_by("-created_at").all()[:3]

    except Exception as e:
        raise Http404("There is some issue fetching data.try again later")


       # sending the page object to pages
    return render(request,"update-detail-view.html",{"update":update_obj,"latest_updates":latest_updates,"categories":categories})

    