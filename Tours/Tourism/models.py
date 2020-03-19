from django.db import models


class Places(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField()


# student_dob = models.DateTimeField('date published')
# Create your models here.
