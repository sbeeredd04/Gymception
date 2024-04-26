from django.urls import path, include
from . import views
from .views import list_equipment, equipment_detail, join_queue
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('equipment/<int:equipment_id>/join/', views.join_queue, name='join-queue'),
    path('equipment/<int:equipment_id>/queue/', views.view_queue, name='view-queue'),
    path('equipment/', list_equipment, name='list-equipment'),
    path('equipment/<int:equipment_id>/', equipment_detail, name='equipment-detail'),
    path('equipment/<int:equipment_id>/join/', join_queue, name='join-queue'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('equipment/<int:equipment_id>/leave/', views.leave_queue, name='leave-queue'),

]
