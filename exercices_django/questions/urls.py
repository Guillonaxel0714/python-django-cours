from django.urls import path
from . import views
app_name = 'questions'
urlpatterns = [
    path('', views.index, name='index'), 
    path('add/', views.add, name='add'),
    path('edit/<int:question_id>/', views.edit, name='edit'),
    path('delete/<int:question_id>/', views.delete, name='delete'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:question_id>/', views.update, name='update'),
]