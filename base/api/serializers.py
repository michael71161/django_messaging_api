from rest_framework.serializers import ModelSerializer
from .models import Message 
from django.contrib.auth.models import User

#we will use and expose  all the fields of this model
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


#we will expose to user only this fields of the model
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

