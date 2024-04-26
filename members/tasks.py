# members/tasks.py
from celery import shared_task
from django.utils import timezone
from .models import EquipmentQueue, PushNotificationSubscription
from django.conf import settings
from gymception.celery import app
from .models import EquipmentQueue
from django.utils import timezone
from django.db.models import F

@app.task
def remove_expired_queue_entries():
    # Define the time delta for expiration, e.g., 30 minutes
    time_threshold = timezone.now() - timezone.timedelta(minutes=30)
    
    # Find all queue entries older than the threshold
    expired_entries = EquipmentQueue.objects.filter(join_time__lte=time_threshold)
    
    # Loop through the expired entries, send notification and delete
    for entry in expired_entries:
        subscription = PushNotificationSubscription.objects.filter(user=entry.user).first()
        if subscription:
            subscription.send_push_notification("Your gym queue time has expired.")
        
        entry.delete()
    
    # Optionally, if you want to inform the next user in line that it's their turn
    next_in_line = EquipmentQueue.objects.annotate(
        previous_join_time=F('join_time') - timezone.timedelta(minutes=30)
    ).filter(join_time__gte=timezone.now(), previous_join_time__lt=timezone.now())
    
    for entry in next_in_line:
        subscription = PushNotificationSubscription.objects.filter(user=entry.user).first()
        if subscription:
            subscription.send_push_notification("It's now your turn for the gym equipment!")


from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import EquipmentQueue

@shared_task
def clear_expired_queues():
    expiration_time = timezone.now() - timedelta(minutes=30)  # for a 30-minute threshold
    expired_queues = EquipmentQueue.objects.filter(join_time__lt=expiration_time)
    expired_queues.delete()
