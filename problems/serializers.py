from rest_framework import serializers
from problems.models import Problem, User


class ProblemSerializer(serializers.ModelSerializer):

    ratio = serializers.SerializerMethodField()
    source = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Problem
        fields = '__all__'

    def get_ratio(self, obj):
        if obj.submitted == 0:
            return 0
        return int(100 * obj.accepted / obj.submitted)


class UserSerializer(serializers.ModelSerializer):

    problem = serializers.SlugRelatedField(many=True,
                                           read_only=True,
                                           slug_field='keyword')

    class Meta:
        model = User
        fields = '__all__'
