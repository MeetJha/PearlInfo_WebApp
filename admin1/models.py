from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
    id = models.AutoField
    user = models.ForeignKey(User, default="0", on_delete=models.CASCADE)
    address = models.TextField(max_length="100", default="")
    phone_no = models.IntegerField(default="0")
    dob = models.DateField()
   
