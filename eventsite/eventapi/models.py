from django.db import models

# Create your models here.
class Event(models.Model):
    #ID event identifer
    models.AutoField("ID",primary_key=True)
    name = models.CharField("Name",max_length=255)
    location = models.CharField("Location",max_length=255)
    start_time = models.DateTimeField("Start Time")
    end_time = models.DateTimeField("End Time")
    visitors = models.ManyToManyField('Visitor', through='Registration')

    def __str__(self):
        return self.name

class Visitor(models.Model):
    email = models.EmailField("E-mail",max_length=254,unique=True)
    events = models.ManyToManyField(Event, through='Registration')

    def __str__(self):
        return self.email

class Registration(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_time = models.DateTimeField("Registration Time",auto_now_add=True)

    def __str__(self):
        return self.registration_time
    
    class Meta:
        unique_together = ['visitor','event']

