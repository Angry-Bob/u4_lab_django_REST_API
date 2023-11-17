from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('Player/', views.PlayerList.as_view(), name='player_list'),
    path('Player/<int:pk>', views.PlayerDetail.as_view(), name='player_detail'),
    path('Team/', views.TeamList.as_view(), name='team_list'),
    path('Team/<int:pk>', views.TeamDetail.as_view(), name='team_detail'),
    path('Conference/', views.TeamList.as_view(), name='team_list'),
    path('Conference/<int:pk>', views.TeamDetail.as_view(), name='team_detail')
]


