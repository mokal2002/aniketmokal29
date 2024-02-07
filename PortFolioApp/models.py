from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50 , default='')
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class MySkills(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    link = models.TextField(max_length=150)
    logo = models.TextField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
class MyPortfolio(models.Model):
    name = models.CharField(max_length=100)
    technology = models.CharField(max_length=50 , default='')
    description = models.TextField(max_length=1000)
    link = models.TextField(max_length=150)
    image = models.ImageField(upload_to="media/images" , default="")
    
    def __str__(self) -> str:
        return self.name
    
    
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review = models.TextField(max_length=400)
    read = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return self.name


    
