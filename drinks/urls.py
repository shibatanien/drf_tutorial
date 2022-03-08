from django.urls import path, include
from . import views

urlpatterns = [
    path('drinks/', views.DrinkList.as_view()),
    path('drinks/<int:pk>/', views.DrinkDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view())
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]