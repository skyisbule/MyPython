from django.db import models

class person(models.Model):
    name = models.CharField(max_length=30)
    result = models.CharField(max_length=300)
    problem = models.CharField(max_length=300)
    zj = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add = True)
