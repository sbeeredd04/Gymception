# members/management/commands/cleanup_queue.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from members.models import EquipmentQueue, PushNotificationSubscription

class Command(BaseCommand):
    help = 'Remove users from the queue after 30 minutes'

    def handle(self, *args, **options):
        thirty_minutes_ago = timezone.now() - timedelta(minutes=30)
        expired_queues = EquipmentQueue.objects.filter(start_time__lte=thirty_minutes_ago)

        for queue in expired_queues:
            # Get the subscription for the user
            try:
                subscription = PushNotificationSubscription.objects.get(user=queue.user)
                # Send a push notification
                subscription.send_push_notification('Your time has ended.')
            except PushNotificationSubscription.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'No subscription found for user {queue.user.username}'))
            # Assuming you have logic to find the next user in queue and notify them

        expired_queues.delete()
        self.stdout.write(self.style.SUCCESS('Successfully removed expired queues'))
