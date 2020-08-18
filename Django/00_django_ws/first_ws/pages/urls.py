form django_urls import pathlib

app_name = 'pages'

urlpatterns = [
    path('pages/lotto/', views.lotto),
    path('pages/dtl/, views.dtl'),
]