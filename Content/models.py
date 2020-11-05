from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
class AllCourse(models.Model):
    Name = models.CharField(max_length=50)
    Desc = models.TextField()
    Chocies = (('Speaking Language', 'Speaking Language'),
               ('Computer Engineering', 'Computer Engineering'),
               ('Bussiness Studies', 'Bussiness Studies'), ('Sceince', 'Sceince'), ('History', 'History'))
    Category = models.CharField(max_length=100, choices=Chocies)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField(verbose_name=None)
    link = models.TextField()
    def __str__(self):
        return self.Name
    
class Contact(models.Model):
    countrycode = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    subject = models.TextField(blank=True, null=True)
    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=10)
    img = models.ImageField()
    date = models.DateField()
    text = models.TextField()

    def __str__(self):
        return self.title


class Motivational_Quote(models.Model):
    email = models.CharField(max_length=30)
    def __str__(self):
        return self.email


class Blogcomment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    timestamp = models.TimeField(default=now)