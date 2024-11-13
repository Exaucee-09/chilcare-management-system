from django.urls import path
from . import views

app_name = 'children'

urlpatterns = [
    path('add/', views.add_child, name='add_child'),
    path('', views.child_list, name='child_list'),
    path('edit/<int:pk>/', views.edit_child, name='edit_child'),
    path('delete/<int:pk>/', views.delete_child, name='delete_child'),
]