from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
# creating user models
class User(AbstractUser):
    email = models.EmailField(max_length=50,unique=True,null=False)

    def __str__(self) -> str:
        return self.first_name
    
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
    

class Like(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="likedon")
    user = models.ForeignKey(User,related_name="likedby",on_delete=models.CASCADE)
    class Meta:
        unique_together = ("blog", "user")

    def __str__(self):
        return f"{self.user.first_name} liked on {self.blog.title}"
    
class comment(models.Model):
    blog = models.ForeignKey(Blog,related_name="commentedon",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="commentedby",on_delete=models.CASCADE)
    comment_content = models.TextField()
    def __str__(self):
        return f"{self.user.first_name} commented on {self.blog.title}"

class Dislike(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="Unlikedon")
    user = models.ForeignKey(User,related_name="Unlikedby",on_delete=models.CASCADE)
    class Meta:
        unique_together = ("blog", "user")

    def __str__(self):
        return f"{self.user.first_name} Unliked on {self.blog.title}"

    
    
