from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

@api_view(["POST"])
def student_create(request):
    serializer = StudentSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def student_get(request):
    students = Student.objects.all()

    student_id = request.query_params.get('student_id')
    name = request.query_params.get('name')
    age = request.query_params.get('age')
    gender = request.query_params.get('gender')
    admission_date = request.query_params.get('admission_date')
    email = request.query_params.get('email')

    if student_id:
        students = students.filter(student_id__icontains=student_id)
    if name:
        students = students.filter(name__icontains=name)
    if age:
        students = students.filter(age__icontains=age)
    if gender:
        students = students.filter(gender__icontains=gender)
    if admission_date:
        students = students.filter(admission_date__icontains=admission_date)
    if email:
        students = students.filter(email__icontains=email)

    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(["GET","POST"])
def student_get_by_id(request, id):
    student = get_object_or_404(Student, pk=id)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

@api_view(["DELETE", "POST"])
def student_delete(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["PATCH", "POST"])
def student_update(request, id):
    student = get_object_or_404(Student, pk=id)
    serializer = StudentSerializer(student, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)