# from django.contrib.auth.models import User
# from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'groups','fist_name','last_name']


from rest_framework import serializers
from .models import Artist, Work

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)


class ArtistSerializer(serializers.ModelSerializer):
   # print("i am here")
    class Meta:
        model = Artist
        fields = '__all__'

    def create(self, validated_data):
        # Get the currently logged-in user from the request context
        user = self.context['request'].user

        # Create the Artist object and associate it with the user
        artist = Artist.objects.create(name=validated_data['name'], user_instance=user)
        return artist


class WorkSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True, read_only=True)
    class Meta:
        model = Work
        fields = '__all__'
