from app1.models import Message
from rest_framework.serializers import ModelSerializer

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
                                                                                from app1.models import Message
from rest_framework.serializers import ModelSerializer

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
