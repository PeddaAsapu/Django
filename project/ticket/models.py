from django.db import models

#class UniqueID(models.Model):
#    id = models.UUIDField(default=uuid.uuid4, editable=False)

class Passenger(models.Model):
 #   uid = models.ForeignKey(UniqueID,primary_key=True,on_delete=models.CASCADE)
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHERS = 'O'

    GENDER_CHOICES = [
        (GENDER_MALE,'Male'),
        (GENDER_FEMALE,'Female'),
        (GENDER_OTHERS,'Others'),
    ]
    passenger_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1,choices =GENDER_CHOICES,default=GENDER_OTHERS )
    age = models.IntegerField()
    dob = models.DateField('Date of Birth')
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    
    def __str__(self):
        return self.passenger_name
    
    
    