from django.urls import path

from api.views import PersonView, PersonSingleView, ProjectSingleView, ProjectView

urlpatterns = [
    path("people", PersonView.as_view()),
    path("people/<int:pk>", PersonSingleView.as_view()),
    path("projects", ProjectView.as_view()),
    path("projects/<int:pk>", ProjectSingleView.as_view()),
]
