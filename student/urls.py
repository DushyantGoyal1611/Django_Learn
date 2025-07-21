from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.StudentView.as_view(), name='student'),
#     path('<int:id>/', views.StudentDetailView.as_view(), name='student-detail')
# ]

# urlpatterns = [
#     path('', views.student_list_create, name='student'),
#     path('<int:id>/', views.student_detail, name='student-deta')
# ]

urlpatterns = [
    path('', views.student_get, name='student_get'),
    path('create/', views.student_create, name='student_create'),
    path('<int:id>/', views.student_get_by_id, name='student_get_by_id'),
    path('<int:id>/delete/', views.student_delete, name='student_delete'),
    path('<int:id>/update/', views.student_update, name='student_update'),
]