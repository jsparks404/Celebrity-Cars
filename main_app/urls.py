from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('celebrities/', views.Celebrities.as_view(), name="celebrity_list"),
    path('new/', views.CelebrityCreate.as_view(), name="celebrity_create"),
    path('celebrities/<int:pk>/', views.CelebrityDetail.as_view(), name="celebrity_detail"),
    path('<int:pk>/delete/', views.CelebrityDelete.as_view(), name="celebrity_delete"),
    path('<int:pk>/new/', views.CarCreate.as_view(), name="car_create"),
    path('celebrities/<int:car_pk>/cars/<int:pk>/', views.CarDetail.as_view(), name="car_detail"),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name="car_update"),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name="car_delete")

]

