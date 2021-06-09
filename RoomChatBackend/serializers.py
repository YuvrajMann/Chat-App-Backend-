from roomChatBackend.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password', 'name', 'phone_number']
        write_only_fields = ('password',)
        read_only_fields = ('id',)
    
    def create(self, validated_data):
        user = super(UserSerializers, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user