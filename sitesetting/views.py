from django.shortcuts import render
from .models import *
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
   
   
   banner=get_banner_by_name("main-banner1")
   giveaway_obj=Giveaway.objects.filter(result_announced="False").order_by("result_announcement_date").all()[0]
   reg_qs=giveaway_obj.giveawayregistration_set.values("player__name")[:50]
   print(reg_qs)
   wheeldata=[]
   colors=list(matplotlib.colors.cnames.values())

   for i,item in enumerate(reg_qs):
      
      wheeldata.append({'text' :str(item["player__name"]), "fillStyle":str(colors[i])})

   



   

   
   delta = giveaway_obj.result_announcement_date-datetime.now(timezone.utc)  
   time_diff=delta.total_seconds()


   return render(request,"landing.html",{"banner":banner,"giveaway":giveaway_obj,"time_diff":time_diff,"wheel_data":json.dumps(wheeldata),"len":len(wheeldata)})
    

