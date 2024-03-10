from django.db import models

# Create your models here.

class Contactform(models.Model):
    Name = models.CharField(max_length = 100,null=False,blank=False)
    Email = models.EmailField()
    Subject = models.CharField(max_length = 255,null=True,blank=True)
    Message = models.TextField()

    def __str__(self):
        return self.Name
