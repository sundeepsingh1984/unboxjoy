from importlib.resources import path
from tkinter import CASCADE
from xmlrpc.client import DateTime
from django.db import models
from sqlalchemy import null
from django_quill.fields import QuillField
from django.urls import reverse
# Create your models here

#Games Model
class Games(models.Model):

    #primary-key
    game_id= models.AutoField(primary_key=True) 
    #columns
    game_name=models.CharField(null=False,blank=False,unique=True,max_length=250)
    game_description=QuillField(null=False,blank=False)
    play_link=models.URLField(null=False,blank=False, max_length=200)
    game_landing_page_link=models.URLField(null=False,blank=False)
    game_cover=models.ImageField(upload_to="games/images")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f'{self.game_name}({self.game_id})'


  

class GameUpdateType(models.Model):
    #primary-key
    update_type_id=models.AutoField(primary_key=True)
    #game
    game=models.ForeignKey(Games,on_delete=models.CASCADE)
    #columns
    update_type_name=models.CharField(null=False,blank=False,max_length=100)

    
    def __str__(self):
        return f'{self.update_type_name}({self.update_type_id})'






class GameUpdates(models.Model):
    #primary-key
    update_id=models.AutoField(primary_key=True)
    #foreign_key
    update_for=models.ForeignKey(Games,on_delete=models.CASCADE)
    update_type=models.ForeignKey(GameUpdateType,on_delete=models.CASCADE)
    #columns
    update_title=models.CharField(max_length=200,null=False,blank=False)
    update_description=QuillField(null=False,blank=False)
    update_link=models.URLField(null=True,blank=True)
    update_thumbnail=models.ImageField(upload_to="games/update/images")
    update_cover=models.ImageField(upload_to="games/update/images")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f'{self.update_title}({self.update_id})'



    def get_absolute_url(self):
        return reverse("games:game-update-details-view", kwargs={"update_id": self.update_id})
    

