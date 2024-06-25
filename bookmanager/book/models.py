from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name
class PeopleInfo(models.Model):
    name=models.CharField(max_length=128)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
