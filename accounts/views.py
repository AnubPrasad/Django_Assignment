# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions
# from django.contrib.auth.models import User
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response

# class ListUsers(APIView):
#     """
#     View to list all users in the system.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAdminUser]

#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)
    

# class CustomAuthToken(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User  # Import the User model
from django import forms
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.status import HTTP_401_UNAUTHORIZED
from .serializers import UserSerializer

from rest_framework.authtoken.views import ObtainAuthToken


from rest_framework import generics
from rest_framework.filters import SearchFilter
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WorkSerializer

from django.contrib.auth import get_user

from rest_framework.generics import CreateAPIView

from django.contrib.auth.models import User  

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)

class UserRegistrationView(APIView):
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if the username already exists in the database
            if User.objects.filter(username=username).exists():
                return Response({"message": "Username already exists. Please choose a different username."},
                                status=status.HTTP_400_BAD_REQUEST)

            # Create a new user in the database
            user = User.objects.create_user(username=username, password=password)
            return Response({"message": "User registered successfully and it is used for Artist Name also."},
                            status=status.HTTP_201_CREATED)

        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        if response.status_code == 200:
            token = response.data['token']
            return Response({'token': token})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)
        


class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [SearchFilter]
    search_fields = ['artists__name', 'link']

class WorkFilterListView(generics.ListAPIView):
    serializer_class = WorkSerializer

    def get_queryset(self):
        work_type = self.kwargs['work_type']
        return Work.objects.filter(work_type=work_type)



class ArtistSearchView(CreateAPIView):
    serializer_class = WorkSerializer

    def create(self, request, *args, **kwargs):
        artist_name = request.data.get('artist', None)
        if artist_name:
            works = Work.objects.filter(artists__name__icontains=artist_name)
            if works.exists():
                serializer = self.get_serializer(works, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "No artist name is present."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Please provide the artist name in the request body as 'artist'."}, status=status.HTTP_400_BAD_REQUEST)





# @api_view(['POST'])
# def new_works(request):
#     serializer = WorkSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Successfully added to the database."})
#     else:
#         return Response(serializer.errors, status=400)

@api_view(['POST'])
def new_works(request):
    # Parse the JSON data for the work and artist
    work_data = request.data.get('work', {})
    artist_data = request.data.get('artist', {})

    # Create the artist and work objects separately
    artist_serializer = ArtistSerializer(data=artist_data, context={'request': request})
    work_serializer = WorkSerializer(data=work_data)

    # Validate and save the artist object
    if artist_serializer.is_valid():
        # Set the user_instance for the Artist to the currently logged-in user
        artist_serializer.validated_data['user_instance'] = request.user
        artist_serializer.save()
        artist_instance = artist_serializer.instance
    else:
        return Response(artist_serializer.errors, status=400)

    # Validate and save the work object
    if work_serializer.is_valid():
        work_serializer.save()
        # Associate the artist with the work
        work_serializer.instance.artists.add(artist_instance)
        return Response({"message": "Successfully added to the database."})
    else:
        # Delete the artist if the work validation fails
        artist_instance.delete()
        return Response(work_serializer.errors, status=400)