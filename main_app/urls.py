from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('new/', views.CelebrityCreate.as_view(), name="celebrity_create"),
    path('<int:pk>/', views.CelebrityDetail.as_view(), name="celebrity_detail"),
    path('<int:car_pk>/cars/<int:pk>/', views.CarDetail.as_view(), name="car_detail"),
]