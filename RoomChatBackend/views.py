from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from roomChatBackend.serializers import UserSerializers
from rest_framework import status

class SignUp(APIView):
      def post(self,request,format=None): 
          resp=UserSerializers(data=request.data)
          if resp.is_valid():
            resp.save()
            return Response(resp.data,status=status.HTTP_201_CREATED)
          else:
            return Response(resp.errors, status=status.HTTP_400_BAD_REQUEST)
          
