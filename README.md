# Ex01 Django ORM Web Application
## Date: 02.02.2026

## AIM
To develop a Django Application to store and retrieve data from an Online Food Delivery Database platform like Zomato or Swiggy using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from .models import customerDB,CustomerDBAdmin
admin.site.register(customerDB,CustomerDBAdmin)
```


## OUTPUT
![alt text](<Screenshot (16).png>)


## RESULT
Thus the program for creating online food delivery website database using ORM hass been executed successfully
