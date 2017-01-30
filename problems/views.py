from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from problems.models import Problem, User
from problems.serializers import ProblemSerializer, UserSerializer


@api_view(['GET'])
def data(request):
    if request.method == 'GET':
        problems = Problem.objects.all()
        serializer = ProblemSerializer(problems, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def user(request, name):
    if request.method == 'GET':
        try:
            user = User.objects.get(name=name)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class IndexView(generic.TemplateView):
    template_name = "problems/index.html"
