from django.contrib import admin
from django.urls import path
from django.urls import include
from members import views as member_views

urlpatterns = [
    #home page view function
    path('', member_views.home_view, name='home'),
    path("admin/", admin.site.urls),
    path('members/', include('members.urls')),
    
]
