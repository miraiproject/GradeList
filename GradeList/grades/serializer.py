from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Grades, Objections, Replies, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class GradesSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Grades
        fields = ('id', 'user', 'english', 'math', 'japanese', 'total', 'gpa')

class ObjectionsSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Objections
        fields = ('id', 'text', 'author', 'created_at')
        read_only_fields = ('created_at',)

class RepliesSerializer(serializers.ModelSerializer):
    target = ObjectionsSerializer()
    author = UserSerializer()
    class Meta:
        model = Replies
        fields = ('id', 'text', 'author', 'created_at', 'target')
        read_only_fields = ('created_at',)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('id', 'name', 'student_number', 'major', 'grade', 'user')
