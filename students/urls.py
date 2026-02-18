from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),

    path('add/', views.add_student, name='add_student'),

    path('<int:pk>/', views.student_detail, name='student_detail'),

    # IMPORTANT: use pk not id
   path('<int:pk>/edit/', views.edit_student, name='edit_student'),


    path('<int:pk>/delete/', views.delete_student, name='delete_student'),

    path('student/<int:pk>/add-achievement/', views.add_achievement, name='add_achievement'),

    path('achievement/<int:id>/edit/', views.edit_achievement, name='edit_achievement'),

    path('achievement/<int:id>/delete/', views.delete_achievement, name='delete_achievement'),

    path('achievement/<int:id>/approve/', views.update_achievement_status,
         {'status': 'Approved'}, name='approve_achievement'),

    path('achievement/<int:id>/reject/', views.update_achievement_status,
         {'status': 'Rejected'}, name='reject_achievement'),
]
