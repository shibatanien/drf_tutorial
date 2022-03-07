from django.urls import path
from . import views

urlpatterns = [
    path('drinks/', views.DrinkList.as_view()),
    path('drinks/<int:pk>/', views.DrinkDetail.as_view())
]