from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Course
from .serializers import CourseSerializer

class CoursesList(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CoursesDetail(RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    