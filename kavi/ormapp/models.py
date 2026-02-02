
from django.db import models
from django.contrib import admin

class customerDB(models.Model):
       OderID=models.IntegerField(primary_key=True);
       C_Name=models.CharField(max_length=25);
       Address=models.CharField(max_length=60);
       Mobile_No=models.IntegerField();
       Amount=models.FloatField();
       Item_Name=models.CharField(max_length=100);
       Oder_Cancellation=models.CharField(max_length=20);

class CustomerDBAdmin(admin.ModelAdmin):
       list_display=['OderID','C_Name','Address','Mobile_No','Amount','Item_Name','Oder_Cancellation'];

