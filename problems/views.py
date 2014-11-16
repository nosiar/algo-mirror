from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from problems.models import Source, Category, Problem
from problems.serializers import ProblemSerializer

@api_view(['GET'])
def data(request):
    if request.method == 'GET':
        problems = Problem.objects.all()
        serializer = ProblemSerializer(problems, many=True)
        return Response(serializer.data)

class IndexView(generic.TemplateView):
    template_name = "problems/index.html"
