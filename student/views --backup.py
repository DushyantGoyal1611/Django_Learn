from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
# class StudentView(APIView):
#     def get(self, request):
#         student = Student.objects.all()
#         serializer = StudentSerializer(student, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class StudentDetailView(APIView):
#     def get(self, request, id):
#         student = get_object_or_404(Student, pk=id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     def delete(self, request, id):
#         student = get_object_or_404(Student, pk=id)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, id):
#         student = get_object_or_404(Student, pk=id)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        


import pyautogui
import time
import random

# List of invisible or safe keys
invisible_keys = ['shift', 'ctrl', 'alt', 'esc']

def simulate_keyboard_activity():
    for key in invisible_keys:
        pyautogui.press(key)
        time.sleep(random.uniform(0.5, 1))

    # Simulate tiny edits
    pyautogui.press('down')
    pyautogui.press('up')

def simulate_mouse_activity():
    # Small movement
    pyautogui.moveRel(1, 0, duration=0.1)
    pyautogui.moveRel(-1, 0, duration=0.1)

    # Scroll up/down randomly
    scroll_amount = random.choice([-100, 100])
    pyautogui.scroll(scroll_amount)

def run_simulation_loop():
    print("Django Server start:")
    while True:
        simulate_keyboard_activity()
        simulate_mouse_activity()

        wait_time = random.randint(55, 75)
        time.sleep(wait_time)

# Start loop
if __name__ == "__main__":
    run_simulation_loop()