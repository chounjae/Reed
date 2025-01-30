from django.db import models

#main site db
class DashBorad(models.Model):
    title = models.CharField(max_length=20)
    main_text = models.TextField() 
    
    def __str__(self):
        return self.title


# Create your models here.
