from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Grades, Objections, Replies, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class GradesSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Grades
        fields = ('user', 'english', 'math', 'japanese', 'total', 'gpa')

class ObjectionsSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Objections
        fields = ('text', 'author', 'created_at')
        read_only_fields = ('created_at',)

class RepliesSerializer(serializers.ModelSerializer):
    target = ObjectionsSerializer()
    class Meta:
        model = Replies
        fields = ('text', 'author', 'created_at', 'target')
        read_only_fields = ('created_at',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'student_number', 'major', 'grade', 'user')
