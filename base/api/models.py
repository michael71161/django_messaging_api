from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    receiver = models.CharField(max_length=50, null=True, blank=True)
    msg_body = models.CharField(max_length=1000, null=True, blank=True)
    msg_subject = models.CharField(max_length=50, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Sender : {self.user}, receiver: {self.receiver}, about :{self.msg_subject}'



