from django.db import models


class Authors(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Books(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    price = models.FloatField(null=True)
    pages = models.IntegerField(null=True)
    language = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.title