from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consumers/', views.consumers_list, name='consumers_list'),
    path('add_consumer/', views.add_consumer, name='add_consumer'),
    path('delete_consumer/<int:consumer_id>/', views.delete_consumer, name='delete_consumer'),
    path('run_query/', views.run_query, name='run_query'),
]
