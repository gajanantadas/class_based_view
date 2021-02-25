from django.urls import path
from . import views
urlpatterns = [
    path('stud/',views.StudentApi.as_view()),
    path('stud/<int:pk>',views.StudentApi.as_view())
]
