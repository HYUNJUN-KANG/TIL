from django.urls import path
from . import views
urlpatterns = [
    path('articles/', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('new/', views.new, name="new"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/edit/", views.edit, name="detail"),
    path("<int:pk>/delete/", views.delete, name="del"),
]