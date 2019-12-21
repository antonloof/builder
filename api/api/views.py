from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from api.models import Person, Project
from api.serializers import PersonSerializer, ProjectSerializer


class PersonView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonSingleView(RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ProjectView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectSingleView(RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

