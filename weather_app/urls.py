from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('delete_city/<int:id_city>', views.delete_city),
]