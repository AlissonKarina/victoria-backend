from rest_framework import serializers
from django.contrib.auth.models import User

from core.models import AnswerQuestion

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, data):
        instance = User()
        instance.first_name = data.get('first_name')
        instance.last_name = data.get('last_name')
        instance.username = data.get('username')
        instance.email = data.get('email')
        instance.set_password(data.get('password'))
        instance.save()
        return instance
            
    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0 :
            raise serializers.ValidationError("Este nombre de usuario ya existe, ingrese uno nuevo")
        else:
            return data

    """ def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) == 1:
            return users
        else:
            raise serializers.ValidationError("Este usuario no existe") """

class AnswerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestion
        fields = ['id', 'answer_text', 'question']
        depth = 1
    
    def create(self, data):
        instance = AnswerQuestion()
        instance.answer_text = data.get('answer_text')
        instance.question = data.get('question')
        instance.save()
        return instance
    
