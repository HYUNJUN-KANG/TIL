from django.urls import path
from . import views
app_name = 'pages'
urlpatterns = [
    path('dinner/<str:dinner>/<int:person>/', views.dinner, name="dinner"),
]