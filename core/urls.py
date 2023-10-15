from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details-project/<int:pk>/', views.project_details, name='details')
]