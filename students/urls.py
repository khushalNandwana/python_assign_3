from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),

    path('api/create-student', views.api_create_student, name='api_create_student'),
    path('api/update-student/<int:id>', views.api_update_student, name='api_update_student'),
    path('api/delete-student/<int:id>', views.api_delete_student, name='api_delete_student'),
    path('api/get-students', views.api_get_students, name='api_get_students'),