from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Count
from django.contrib.auth.models import User

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_min_wait_time(self):
        # Calculate the minimum wait time based on the queue.
        queue_length = self.queue.count()
        return queue_length * 30  # Assuming each user takes up 30 minutes

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
