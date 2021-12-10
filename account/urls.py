from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('users/', views.users),
    # path('users/<int:user_id>', views.user_detail),
    path('users/change_password/', views.change_password),
    # path('users/login/', views.login),
    path('users/login/', views.user_login),
    path('users/profile/', views.profile),
    path('users/<uuid:user_id>/', views.user_detail),
    path('users/signup/', views.add_user),
    path('users/', views.get_user),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
