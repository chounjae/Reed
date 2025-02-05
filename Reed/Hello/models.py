from django.db import models

#main site db
class DashBoard(models.Model):
    title = models.CharField(max_length=20)
    main_text = models.TextField() 
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.title

# Create your models here.
