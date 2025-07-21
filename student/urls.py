from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.StudentView.as_view(), name='student'),
#     path('<int:id>/', views.StudentDetailView.as_view(), name='student-detail')
# ]

urlpatterns = [
    path('', views.student_list_create, name='student'),
    path('<int:id>/', views.student_detail, name='student-detail')
]