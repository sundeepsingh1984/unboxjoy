from django.http import Http404
from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import *
from .forms import ContactRequestForm, SubscribeForm
from django.contrib import messages
from blogs.models import Blog
import random
from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ObjectDoesNotExist
from giveaways.models import Giveaway
from .shortcuts import get_banner_by_name
from django.core import serializers
from datetime import datetime
from datetime import timezone
import matplotlib
import json
import matplotlib
# Create your views here.


def index_view(request):
   #get banner
   banner=get_banner_by_name("main-banner")
   
   #get give away with related objects
   giveaway_obj=Giveaway.objects.filter(result_announced="False").order_by("result_announcement_date").first()
   
   if giveaway_obj:
      reg_qs=giveaway_obj.giveawayregistration_set.order_by("-winner").values("player__name")[:50]
      total_winners=giveaway_obj.giveawayregistration_set.filter(winner="True").count()
   

      #create wheel data for spinning wheel
      wheeldata=[]
      #abstract colours list from matplotlib
      colors=list(matplotlib.colors.cnames.values())
      for i,item in enumerate(reg_qs):
         wheeldata.append({'text' :str(item["player__name"]), "fillStyle":str(colors[random.randrange(1, len(colors))])})
      
      #get time for upcoming data giveaway
      delta = giveaway_obj.result_announcement_date-datetime.now(timezone.utc)  
      time_diff=delta.total_seconds()

   else:
      time_diff=None
      wheeldata=None
      total_winners=None



   #obtain random custom ads 
   ad_qs=list(CustomAdvertisement.objects.filter(active="True").all())
   if ad_qs:
      random_ads = random.sample(ad_qs, 2)

   else:
      random_ads=None


   #BRAND-BANNER
   try: 
      banner_obj=Banner.objects.get(banner_name__istartswith="brand-banner")
      if banner_obj:
         brand_banner=banner_obj.bannerimages_set.all()
   except ObjectDoesNotExist:
      brand_banner=None
      pass




   #Youtube_videos

   youtube_feed_obj=SocialMediaFeedType.objects.filter(feed_type_name__istartswith="youtube").first()

   if youtube_feed_obj:
      youtube_feeds=youtube_feed_obj.feeds_set.order_by("-created_at").all()[:2]


   #trending_blogs
   blog_qs=Blog.objects.filter(trending=True).order_by("-created_at").all()[:3]


   #instagram
   
   insta_feed_obj=SocialMediaFeedType.objects.filter(feed_type_name__istartswith="instagram").first()
   if insta_feed_obj:
      insta_feed=insta_feed_obj.feeds_set.order_by("-created_at").all()[:3]
   
   # return template
   return render(request,"landing.html",{"trending_blogs":blog_qs,"instafeed":insta_feed if insta_feed else None,"youtube_feeds":youtube_feeds if youtube_feeds else None,"brand_banner":brand_banner if brand_banner else None,"ads":random_ads if random_ads else None,"banner":banner,"time_diff":time_diff,"wheel_data":json.dumps(wheeldata) if wheeldata else None,"len":len(wheeldata) if wheeldata else None,"winner_in_list":total_winners })
    

def info_view(request,id):

   try:
      info=ImportantLink.objects.get(id=id)

      if info.link_name == "contact" or info.link_name == "contact us":

         form=ContactRequestForm()
         return render(request,"info.html",{"info":info,"form":form})



      return render(request,"info.html",{"info":info})

   except Exception as e:

      return Http404("Oops!.There was some issue fecting info please try again later")


def contact_request(request):
   if request.method == "POST":
      contact_form=ContactRequestForm(request.POST)

      if contact_form.is_valid():
            contact_form.save()
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [request.business_info.email])
                messages.add_message(request,messages.WARNING,"Thanks! for contacting our team will get in touch soon")

            except Exception as e:
                messages.add_message(request,messages.WARNING,"There was some issue our team will get in touch soon")

      
            
   
               
      return render(request,"info.html",{"form":contact_form,"form_redirect":True})      
   

def subscribe_newsletter(request):
   if request.method == "POST":
      subs_frm=SubscribeForm(request.POST)
      
      if subs_frm.is_valid():
         subs_frm.save()
         messages.add_message(request,messages.SUCCESS,"Thanks! for subscribing to our newsletters")
         request.session['subscribed'] = True
      
      else:
         request.session['hide'] = True
         messages.add_message(request,messages.WARNING,"Already Subscribed With This Email ID")
         
      return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

