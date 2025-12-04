from django.urls import path
from .views import home, delete_todo

urlpatterns = [
    path('', home, name="home"),
    path('delete/<int:id>/', delete_todo, name='delete_todo'),
]