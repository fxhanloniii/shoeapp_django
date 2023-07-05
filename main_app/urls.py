from django.urls import path 
from . import views 

# this like app.use() in express 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('collection/', views.CollectionList.as_view(), name='collection'),
    path('shoes/new/', views.ShoeCreate.as_view(), name="shoe_create"),
    path('shoes/<int:pk>/', views.ShoeDetail.as_view(), name="shoe_detail"),
    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoe_update'),
    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoe_delete'),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]