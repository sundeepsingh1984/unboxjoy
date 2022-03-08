
from django.db import models
from sqlalchemy import null
from django_quill.fields import QuillField
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from django.urls import reverse


# Create your models here.

#GiveAway Category Model
class GiveawayCategory(models.Model):
    gawy_cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(blank=True,null=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





 






# GiveAway Model
class Giveaway(models.Model):
    giveaway_id = models.AutoField(primary_key=True)
    giveaway_cat = models.ForeignKey(GiveawayCategory,on_delete=models.CASCADE)
    giveaway_title=models.CharField(max_length=200,blank=True,null=True)
    giveaway_desc=QuillField()
    last_apply_date=models.DateTimeField(blank=True,null=True)
    result_announcement_date=models.DateTimeField(blank=False,null=True)
    result_announced=models.BooleanField(default=False)
    total_winners=models.IntegerField(blank=False,null=False)
    redirect_url=models.URLField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    
    def __str__(self):
        return f'{self.giveaway_title}({self.giveaway_id})'



    def get_absolute_url(self):
        return reverse("giveaways:giveaway-detail", kwargs={"gawy_id": self.giveaway_id})
        
    




class Player(models.Model):
    player_id=models.CharField(max_length=100,blank=False,null=False,unique=True)
    name=models.CharField(max_length=100,blank=False,null=False)
    email_id=models.EmailField(unique=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    profile_image=models.ImageField(upload_to="giveaway/profiles",blank=True,null=True)
    country=CountryField()
    address=models.TextField(blank="False",null="False")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    
    def __str__(self):
        return f'{self.name}({self.player_id})'


       

class GiveawayRegistration(models.Model):
    reg_id=models.AutoField(primary_key=True)
    giveaway=models.ForeignKey(Giveaway,on_delete=models.CASCADE)
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    winner=models.BooleanField(default=False,blank="False",null="False")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

  
 
    def __str__(self):
        return f'{self.player.name}({self.reg_id})'

    





class Winners(models.Model):
    id=models.AutoField(primary_key=True)
    giveaway=models.ForeignKey(Giveaway,on_delete=models.CASCADE)
    winner=models.ForeignKey(Player,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.winner.name}({self.id})'


    class Meta:
        unique_together = ('giveaway', 'winner')









    