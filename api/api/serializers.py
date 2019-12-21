from rest_framework.serializers import ModelSerializer

from api.models import Person, Project


class PersonSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Person


class ProjectSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Project
