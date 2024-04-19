# members/management/commands/add_equipment.py
from django.core.management.base import BaseCommand
from members.models import Equipment

class Command(BaseCommand):
    help = 'Adds new equipment to the database'

    def add_arguments(self, parser):
        # Adding command-line arguments for equipment name and description
        parser.add_argument('name', type=str, help='The name of the equipment')
        parser.add_argument('description', type=str, help='The description of the equipment')

    def handle(self, *args, **options):
        name = options['name']
        description = options['description']
        
        # Check if the equipment already exists
        if Equipment.objects.filter(name=name).exists():
            self.stdout.write(self.style.WARNING('Equipment already exists.'))
        else:
            # Create new equipment instance
            equipment = Equipment(name=name, description=description)
            equipment.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully added equipment "{name}"'))
