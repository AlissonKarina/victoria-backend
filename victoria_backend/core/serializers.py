from rest_framework import serializers
from django.contrib.auth.models import User

from core.models import AnswerQuestion, Paper, AnswerText, Parameter, Question

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

class PaperSerializer(serializers.ModelSerializer):
    answer_texts = serializers.SlugRelatedField(
        many=True, 
        read_only=True, 
        slug_field='answer_text'
    )
    class Meta:
        model = Paper
        fields = [
            'id', 'title', 'authors', 'year', 
            'treatment', 'description', 'pdf', 'answer_texts'     
        ]
        depth = 1
    
    def create(self, data):
        instance = Paper()
        instance.title = data.get('title')
        instance.authors = data.get('authors')
        instance.year = data.get('year')
        instance.treatment = data.get('treatment')
        instance.pdf = data.get('pdf')
        instance.description = data.get('description')
        instance.save()
        return instance
        
""" class AnswerTextListSerializer(serializers.ListSerializer): 
    paper = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Paper.objects.all())
    class Meta:
        fields = [
                'id', 'answer_text', 'paper'  
            ]
    def create(self, data):
        papers = [Paper(**item) for item in data]
        return Paper.objects.bulk_create(papers) """

class AnswerTextSerializer(serializers.ModelSerializer):
    paper = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Paper.objects.all())
    class Meta:
        model = AnswerText
        """ list_serializer_class = AnswerTextListSerializer """
        fields = [
            'id', 'answer_text', 'paper'   
        ]
        depth = 1
    
    def create(self, data):
        instance = AnswerText()
        instance.answer_text = data.get('answer_text')
        instance.paper = data.get('paper')
        instance.save()
        return instance

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = [
            'id', 'keratometry', 'pachymetry', 
            'cdva', 'udva', 'grade'
        ]
        depth = 1
    
    def create(self, data):
        instance = Parameter()
        instance.keratometry = data.get('keratometry')
        instance.pachymetry = data.get('pachymetry')
        instance.cdva = data.get('cdva')
        instance.udva = data.get('udva')
        instance.grade = data.get('grade')
        instance.save()
        return instance

class QuestionSerializer(serializers.ModelSerializer):
    parameter = ParameterSerializer(many=True)
    answer_text = serializers.PrimaryKeyRelatedField(write_only=True, queryset=AnswerText.objects.all())
    class Meta:
        model = Question
        fields = [
            'id', 'question', 'answer', 'parameter', 'answer_text'
        ]
        depth = 1
    
    def create(self, data):
        instance = Question()
        instance.question = data.get('question')
        instance.answer = data.get('answer')
        instance.parameter = data.get('parameter')
        instance.answer_text = data.get("answer_text")
        instance.save()
        return instance


