from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:program_id>/', views.detail, name='detail'),
    path('<int:program_id>/results/', views.results, name='results'),
    path('<int:program_id>/start/', views.start, name='start'),
    path('<int:program_id>/stop/', views.stop, name='stop'),
]