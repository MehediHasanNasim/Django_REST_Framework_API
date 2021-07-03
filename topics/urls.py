from django.urls import path
from .import views 


urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('list/', views.topicList, name='list'),
    path('detail/<str:pk>/', views.topicDetail, name='detail'),
    path('create/', views.topicCreate, name='create'),
    path('update/<str:pk>/', views.topicUpdate, name='update'),
    path('delete/<str:pk>/', views.topicDelete, name='delete'),
    

]