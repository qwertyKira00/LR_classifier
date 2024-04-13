from django.contrib import admin
from django.urls import path

from .views import input_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('input/', input_view, name='input')
]
