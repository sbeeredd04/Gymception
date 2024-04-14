from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

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
