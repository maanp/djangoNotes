from django.db import models

# Create your models here.
class Notes(models.Model):
    # sno = models.AutoField()
    title = models.CharField(max_length=50)
    desc = models.TextField()
    time=models.TimeField()


    def __str__(self):
        return self.title


