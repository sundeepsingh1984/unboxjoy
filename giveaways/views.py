from email import message
from email.policy import HTTP
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Giveaway, GiveawayRegistration, Player
from django.utils import timezone
from .shortcuts import divide_chunks
from .forms import PlayerForm
from sitesetting.shortcuts import get_banner_by_name
from django.contrib import messages
# Create your views here.
from django import template
register = template.Library()


@register.filter
def in_winners(registrations ):
    return registrations.filter(winner="True")






def giveaway_catogorical_view(request,cat_id):

    try:
        today = timezone.now() 
        active_give_aways=Giveaway.objects.filter(giveaway_cat =cat_id, result_announced = False,last_apply_date__gte =today).order_by('last_apply_date').all()
        announced_giveaways=Giveaway.objects.filter( giveaway_cat=cat_id,result_announced = True).order_by('last_apply_date').all()[:12]
        active_give_aways=list(divide_chunks(active_give_aways,3))
        announced_giveaways=list(divide_chunks(announced_giveaways,3))
        banner=get_banner_by_name("giveaway-banner")

  
        return render(request,'giveaway-view.html',{"active_giveaways":active_give_aways,"announced_giveaways":announced_giveaways,"banner":banner})
    
    except Exception as e:
        raise e
        

    
def giveaway_detail_view(request,gawy_id):
    giveaway=get_object_or_404( Giveaway,giveaway_id =gawy_id )
    announced_giveaways=Giveaway.objects.filter( giveaway_cat=giveaway.giveaway_cat.gawy_cat_id,result_announced = True).order_by('last_apply_date').all()[:12]
    announced_giveaways=list(divide_chunks(announced_giveaways,3))   
    return render(request,"giveaway-detail-view.html",{"details":giveaway,"announced_giveaways":announced_giveaways})
    


def verify_and_register_player(request):
    if request.method == "POST":
        if Player.objects.filter(player_id = request.POST.get("p_id")).exists():
            player_obj=Player.objects.filter(player_id = request.POST.get("p_id")).get()
            
            if GiveawayRegistration.objects.filter(giveaway_id=request.POST.get("g_id"),player=player_obj.id).exists():
                messages.add_message(request,messages.INFO,"Already Registered for this Giveaway")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            else:

                try:

                    giveaway_obj=Giveaway.objects.get(giveaway_id=request.POST.get("g_id"))
                    reg_obj=GiveawayRegistration(giveaway_id=giveaway_obj.giveaway_id,player=player_obj)
                    reg_obj.save()
                    messages.add_message(request,messages.SUCCESS,"Thanks for Enrolling into Giveaway.You will get Notified for the results.")
                    
                    g_type=str(giveaway_obj.giveaway_cat.cat_name).lower()
                    
                    if g_type == "video giveaway":

                       return redirect(giveaway_obj.redirect_url)

                    else:    
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                   

                except Exception as e:

                    raise Http404(e)
        


        else:
            form=PlayerForm()
            messages.add_message(request,messages.INFO,"Sorry! Seems this is the first time you are applying for giveaway,please submit your details")
            return render(request,"player-registration-view.html",{"form":form,"giveaway_id":request.POST.get("g_id"),"message":"Oops!. Seems You Are Participating For First Time Please Provide Some Information About Yourself"})





def register_player(request):
    if request.method == "POST":
        player_frm=PlayerForm(request.POST)
        g_id=request.POST["giveaway_id"]
        p_id=request.POST["player_id"]

        if player_frm.is_valid():
           
            player_frm.save()
            request.session["player_id"]=p_id
                
                
            messages.add_message(request,messages.SUCCESS,"Profile Created SucessFully.")
            if g_id:
                try:
                    giveaway_obj=Giveaway.objects.get(giveaway_id=int(g_id))
                    player_obj=Player.objects.get(player_id=p_id)
                    reg = GiveawayRegistration(giveaway_id=int(g_id),player=player_obj)
                    messages.add_message(request,messages.SUCCESS,"Registerd for Giveaway SucessFully.")
                    reg.save()
                    g_type=str(giveaway_obj.giveaway_cat.cat_name).lower()
                    if g_type == "video giveaway":

                       return redirect(giveaway_obj.redirect_url)

                    else:    
                        return HttpResponseRedirect(reverse("giveaways:giveaway-detail",args=(g_id,)))
                    
                    
                   
                except Exception as e:
                    raise Http404(e)
       
            else:

                return HttpResponseRedirect(reverse("index"))     


        else:
            return render(request,"player-registration-view.html",{"form":player_frm,"giveaway_id":g_id})






