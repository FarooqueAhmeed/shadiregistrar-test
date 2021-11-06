from rest_framework import serializers
from app.models import Private,Public




class PrivateSerializer(serializers.ModelSerializer):


    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'DOF', 'age')
        model = Private



class PublicSerializer(serializers.ModelSerializer):


    class Meta:
        fields = ('id', 'url', 'name')
        model = Public


