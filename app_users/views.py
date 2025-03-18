from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Teacher, Student
from .serializers import TeacherSerializer, StudentSerializer, UserSerializer

# --- User API ---
class UserListView(generics.ListAPIView):
    """Foydalanuvchilar ro‘yxatini olish"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Bitta foydalanuvchini ko‘rish, yangilash va o‘chirish"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# --- Teacher API ---
class TeacherListCreateView(generics.ListCreateAPIView):
    """O‘qituvchilarni olish va yangi o‘qituvchi yaratish"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Bitta o‘qituvchi ma’lumotlarini ko‘rish, yangilash va o‘chirish"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

# --- Student API ---
class StudentListCreateView(generics.ListCreateAPIView):
    """Talabalarni olish va yangi talaba yaratish"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Bitta talaba ma’lumotlarini ko‘rish, yangilash va o‘chirish"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
