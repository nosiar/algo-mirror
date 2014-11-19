from rest_framework import serializers
from problems.models import Problem, Category, Source, User

class ProblemSerializer(serializers.ModelSerializer):

    ratio = serializers.SerializerMethodField('get_ratio')
    source = serializers.RelatedField()
    category = serializers.RelatedField(many=True)

    class Meta:
        model = Problem

    def get_ratio(self, obj):
        return int(100 * obj.accepted / obj.submitted)

class UserSerializer(serializers.ModelSerializer):

    problem = serializers.RelatedField(many=True)

    class Meta:
        model = User
