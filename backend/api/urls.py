from django.urls import path
from .views import login, users, delete_user, add_user

urlpatterns = [
    path('login/', login),
    path('users/', users),
    path('delete/<int:id>/', delete_user),
    path('add/', add_user),
]



