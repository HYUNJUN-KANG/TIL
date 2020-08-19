from django.contrib import admin
from .models import Article       # 명시적인 상대경로로써 models 앞에 . 붙임

# Register your models here.
admin.site.register(Article)