from django.db import models

# Create your models here.
class priyanka(models.Model):
    original_url=models.URLField(max_length=700,default='')
    short_url=models.CharField(max_length=100,default='')
    time_date_created=models.DateTimeField()
    
    
    
    def __str__(self):
        return self.original_url
