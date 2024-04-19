from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Count
from django.contrib.auth.models import User
from pywebpush import webpush, WebPushException
import json


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_min_wait_time(self):
        # This method will return the minimum wait time for the equipment by calculating the amount of users in the queue and multiplying it by 30 minutes
        queue_count = self.queue.count()
        print(queue_count)
        return queue_count * 30

class EquipmentQueue(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='queue')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    join_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['join_time']

    def __str__(self):
        return f"{self.user.username} in queue for {self.equipment.name}"

    def get_queue_position(self):
        # This method will return the user's position in the queue
        all_entries = EquipmentQueue.objects.filter(equipment=self.equipment, join_time__lte=self.join_time)
        return all_entries.count()
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username
    
    
class PushNotificationSubscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='push_subscription')
    subscription_info = models.TextField()  # Store the subscription info as a JSON string

    def send_push_notification(self, message):
        # Convert the subscription info from JSON string back to a dictionary
        subscription_info = json.loads(self.subscription_info)
        try:
            # Send the push notification
            webpush(
                subscription_info=subscription_info,
                data=message,
                vapid_private_key=settings.VAPID_PRIVATE_KEY,
                vapid_claims={"sub": "mailto:your-email@example.com"}
            )
        except WebPushException as e:
            # Log the exception or handle it
            pass
        except (ValueError, TypeError) as e:
            # Handle the case where the JSON is malformed or missing
            pass
    
    def __str__(self):
        return f"PushNotificationSubscription for {self.user.username}"