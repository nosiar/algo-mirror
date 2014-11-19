from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from problems.models import Source, Category, Problem, User
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
        user = User.objects.get(name=name)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class IndexView(generic.TemplateView):
    template_name = "problems/index.html"
