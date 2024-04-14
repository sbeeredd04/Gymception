from django.urls import path, include
from . import views
from .views import list_equipment, equipment_detail, join_queue

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('equipment/<int:equipment_id>/join/', views.join_queue, name='join-queue'),
    path('equipment/<int:equipment_id>/queue/', views.view_queue, name='view-queue'),
    path('equipment/', list_equipment, name='list-equipment'),
    path('equipment/<int:equipment_id>/', equipment_detail, name='equipment-detail'),
    path('equipment/<int:equipment_id>/join/', join_queue, name='join-queue'),

]
