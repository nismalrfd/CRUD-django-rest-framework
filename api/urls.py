from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.apiOverview,name='apiOverview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-create/', views.taskCreate, name='task-create'),

    path('task-detail/<int:pk>', views.taskDetali, name='task-detail'),
    path('task-update/<int:pk>', views.taskUpdate, name='task-update'),
    path('task-delete/<int:pk>', views.taskDelete, name='task-delete'),

]
