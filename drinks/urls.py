from django.urls import path, include
from . import views

urlpatterns = [
    path('drinks/', views.DrinkList.as_view(), name='drink_list'),
    path('drinks/<int:pk>/', views.DrinkDetail.as_view(), name='drink_detail'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail')
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]