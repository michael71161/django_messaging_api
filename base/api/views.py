from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth import logout
from .models import Message
from .serializers import MessageSerializer ,UserSerializer

#  methods for testing of routes models and authentication:
@api_view(['GET'])

def index(request):
    return Response ("this is a test route ")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_getall(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


#get list of all usernames 

@api_view(['GET'])
def get_users(request):
    all_users = User.objects.all()
    serializer = UserSerializer(all_users, many=True)
    return Response(serializer.data)




    



# singin, obtain token for the user 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add  our custom claims to token payload 
        token['username'] = user.username
        token['email'] = user.email
        token['isAdmin'] = user.is_superuser
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# register/signup
@api_view(['POST'])
def register(request):
    try:
         User.objects.create_user(username= request.data["username"],email=request.data["email"],password=make_password(request.data["password"]))
         print( request.data["username"] )
         print( request.data["email"])
         return Response("Registration done") 
    except:
        return Response("Something went wrong")
    
   


# Logout using built in django func
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myLogout(request):
    logout(request)
    return Response("user logged out")


# write a new message 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def writeMsg(request):
    user = request.user 
    data = request.data
    #getting objects from request data and performing validation 
    #of the mesaage critical objects 
    msg_bdy = data['msg_body']
    rcv = data['receiver']
    

    if msg_bdy == " " or rcv == " ":
        return Response ({'Error':'Message missing details'},status=status.HTTP_400_BAD_REQUEST)
    else: 

        wrt_msg = Message.objects.create(
            user=user,
            receiver = rcv,
            msg_body = msg_bdy,
            msg_subject = data['msg_subject']
        )
        serializer = MessageSerializer(wrt_msg, many=False)
        return Response(serializer.data)

# get all messages for the logged in user 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllUserMsg(request):
    try:
       user = request.user
       allmsgs = Message.objects.filter(receiver=user)
       serializer = MessageSerializer(allmsgs, many=True)
       return Response(serializer.data)
    except:
        return Response ({'Error':'No Messages'},status=status.HTTP_400_BAD_REQUEST)
     

#read message -return one message and mark as read 

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def markMsgAsRead(request, pk):
    try:
        msg = Message.objects.get(_id=pk)
        msg.is_read = True
        msg.save()
        serializer = MessageSerializer(msg, many=False)
        return Response (serializer.data)
    except:
        return Response({'Error':'out of range'},status=status.HTTP_400_BAD_REQUEST)



# get all unread messages for the logged in user 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllUnrdMsg(request):
    try:
       user = request.user
       allmsgs = Message.objects.filter(receiver=user)
       unrd_msg = allmsgs.filter(is_read = False)
       serializer = MessageSerializer(unrd_msg, many=True)
       return Response(serializer.data)
    except:
        return Response ({'Error':'No Messages'},status=status.HTTP_400_BAD_REQUEST)


# Delete message - by the logged in user 

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delMsgUser(request ,pk):
    try:
        del_msg = Message.objects.get(_id=pk)
        del_msg.delete()
        return Response("Message Deleted")
    except:
        return Response ({'Error':'No Messages found'},status=status.HTTP_400_BAD_REQUEST)

     










    
    
   
    
