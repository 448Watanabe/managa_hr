from django.urls import path
from . import views

app_manage = "manage_hr_app"


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]