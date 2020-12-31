# from rest_framework.views import APIView
# from rest_framework.generics import UpdateAPIView
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework.status import *
# from google.oauth2 import id_token
# from google.auth.transport import requests
# from django.conf import settings
# from google.oauth2 import id_token
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class GoogleAuth(UpdateAPIView):

#     #get id
#     #-> validate with google
#     #if valid
#     #   get user profile data from google
#     #   if email excists
#     #       return error
#     #   else
#     #       if id excist
#     #           login
#     #       else:
#     #           create user
#     #else
#     #   return error

#     def put(self, request, *args, **kwargs):
#         google_id=request.data.get('id_token')
#         if id_token is None:
#             return Response(status=HTTP_406_NOT_ACCEPTABLE)
#         try:
#             idinfo = id_token.verify_oauth2_token(google_id, requests.Request(), settings.GOOGLE_CLIENT)
#             userid = idinfo['sub']
#             useremail= idinfo['email']
#         except ValueError:
#             # Invalid token
#             return Response(status=HTTP_403_FORBIDDEN)
#             pass
        
#         #basicly a hack because im running late with this project and dont want to go through trouble 
#         #of overwriting the base user class and creating platform id's
     
#         if User.objects.filter(username="google"+userid).exists():
#             #login user
#             #username=mail
#             #auth user (username,)
        
#             print(userid)
#         print(useremail)

#         if User.objects.filter(email=useremail).exists():
#             return Response("The provided email is already registret. CREATING FAKE USERS IS AGAINST OUR POLICY!",status=HTTP_409_CONFLICT)

#         return Response(status=HTTP_200_OK)