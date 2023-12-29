from django.db import models
class books(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=100)
    shelf_no = models.CharField(max_length=10)
    author = models.CharField(max_length=100)


    def __str__(self):
        return self.name
