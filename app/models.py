from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone=models.IntegerField(null=True)



class Poll(models.Model):
    question=models.CharField(max_length=250)
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="poll")
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False)


    def __str__(self):
        return self.question

class Choice(models.Model):
    option=models.CharField(max_length=250)
    poll_object=models.ForeignKey(Poll,on_delete=models.CASCADE,related_name='choice')



class Vote(models.Model):
    poll_object=models.ForeignKey(Poll,on_delete=models.CASCADE,related_name='vote')
    choice_object=models.ForeignKey(Choice,on_delete=models.CASCADE,related_name='vote')
    owner_object=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='vote')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together=('poll_object', 'owner_object')







