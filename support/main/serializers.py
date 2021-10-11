from rest_framework.serializers import ModelSerializer

from main.models import User, Support


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'message')


class SupportSerializer(ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'