from django.db import models

# Create your models here.

class Chat(models.Model):
    content = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('group',on_delete=models.CASCADE)



class Group(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
