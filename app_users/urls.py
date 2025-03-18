from django.urls import path
from .views import (
    TeacherListCreateView, TeacherDetailView,
    StudentListCreateView, StudentDetailView,
    UserListView, UserDetailView
)

urlpatterns = [
    # User (Foydalanuvchilar)
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),

    # Teacher (O‘qituvchilar)
    path('teachers/', TeacherListCreateView.as_view(), name='teacher_list_create'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),

    # Student (Talabalar)
    path('students/', StudentListCreateView.as_view(), name='student_list_create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
]
