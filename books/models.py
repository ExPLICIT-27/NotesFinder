from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class Module(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='modules')
    name = models.CharField(max_length = 255)
    file_path = models.CharField(max_length=500)
    
    def __str__(self):
        return f"{self.subject.name} - {self.name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_picture = models.ImageField(upload_to = 'profile_pics/')
    
    def __str__(self):
        return self.user.username
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'subject')
        
    def __str__(self):
        return f"{self.user.username} - {self.subject.name}"
    