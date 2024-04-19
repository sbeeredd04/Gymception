# Gymception

TO ADD EQUIPMENT : 

python manage.py shell

``` Run script : 
from members.models import Equipment

# List of tuples containing the equipment name and a short description
equipment_list = [
    ("Treadmill", "A machine for walking or running."),
    ("Stationary Bike", "A bike for cardio workout."),
    ("Rowing Machine", "Simulates the action of watercraft rowing."),
    # ... Add all other equipments similarly
]

for name, description in equipment_list:
    Equipment.objects.get_or_create(name=name, description=description)

print("Equipment has been added to the database.")
``