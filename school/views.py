from rest_framework import viewsets, generics
from school.models import Student, Course, Registration
from .serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListStudentRegistrationsSerializer, ListRegisteredStudentsSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    """Showing all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    """Showing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationsViewSet(viewsets.ModelViewSet):
    """Showing all registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class ListStudentRegistrations(generics.ListAPIView):
    """Showing a student's registrations"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentRegistrationsSerializer

class ListRegisteredStudents(generics.ListAPIView):
    """Showing all students registered in a course"""
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegisteredStudentsSerializer
