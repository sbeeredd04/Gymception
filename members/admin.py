from django.contrib import admin
from django.contrib import admin
from .models import Equipment, EquipmentQueue

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(EquipmentQueue)
class EquipmentQueueAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'user', 'join_time']
    list_filter = ['equipment', 'join_time']
