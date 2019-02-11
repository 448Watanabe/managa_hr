from django.urls import path
from . import views

app_name = "manage_hr_app"


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
]