from rest_framework import serializers
from .models import Contact, Group


class ContactSerializer(serializers.ModelSerializer):

    class Meta:

        model = Contact
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    contacts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:

        model = Group
        fields = ('name', 'contacts')
