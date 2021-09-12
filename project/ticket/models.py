import uuid
from django.db import models

# Create your models here.



class Gender(models.Model):
    gender = models.CharField(max_length=200)
    
    def __str__(self):
        return self.gender



#class UniqueID(models.Model):
#    id = models.UUIDField(default=uuid.uuid4, editable=False)

class Passenger(models.Model):
 #   uid = models.ForeignKey(UniqueID,primary_key=True,on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=200)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    age = models.IntegerField()
    dob = models.DateTimeField('Date of Birth')
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)

    def __str__(self):
        return self.passenger_name
    