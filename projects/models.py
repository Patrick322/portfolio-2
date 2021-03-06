from django.db import models
import datetime as dt

# Create your models here.
class projects(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name
    class meta:
        ordering =['name']
    
    def save_editor(self):
        self.save()


class description(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name