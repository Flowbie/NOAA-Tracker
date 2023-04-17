# Dolan, Austin
# ICS 110P Final Exam Program
# December 12 2022
# Program represents a program that a company like NOAA could use to update data logs for animal's they are currently tracking
# Allows user to view animal's attributes, view distance traveled since last update, and update log of last known location
# Keeps track of animal's health status, age, length, breed, and id number


from math import radians, cos, sin, asin, sqrt

# Classes
class Shark():
	def __init__(self, id_num, breed, length, region, age, DD_lat, DD_long, healthy = True):
		self.id_num = id_num 
		self.breed = breed
		self.length = length
		self.region = region
		self.age = age
		self.DD_lat = DD_lat
		self.DD_long = DD_long
		self.healthy = healthy

	def __str__(self):
		shark_stats = '\n\n   ***Shark Description***'
		shark_stats += '\n\tID Number: ' + str(self.id_num)
		shark_stats += '\n\tBreed: ' + self.breed
		shark_stats += '\n\tLength(ft): ' + str(self.length)
		shark_stats += '\n\tRegion: ' + self.region
		shark_stats += '\n\tAge: ' + str(self.age)
		shark_stats += '\n\tLast Known Location: ' + str(self.DD_lat) + ', ' + str(self.DD_long)
		shark_stats += '\n\tHealthy: ' + str(self.healthy)
		return shark_stats

	# Warning function to alert user if location since last update hasn't changed, will also update healthy status to false
	def warning(self, new_location):
		# Produce a warning if shark location has not changed since last update
		last_known_location = f'{self.DD_lat}, {self.DD_long}'
		if last_known_location == new_location:
			warning = f'Warning! Shark({self.id_num}) might be deceased, has not reported movement since last update.'
			setattr(self, 'healthy', False)
		else:
			warning = 'No warnings to report'
		return warning

class Turtle():
	def __init__(self, id_num, breed, length, limbs_num, endangered, DD_lat, DD_long, healthy = True):
		self.id_num = id_num
		self.breed = breed
		self.length = length
		self.limbs_num = limbs_num
		self.endangered = endangered
		self.DD_lat = DD_lat
		self.DD_long = DD_long
		self.healthy = True

	def __str__(self):
		turtle_stats = '\n\n   ***Turtle Description***'
		turtle_stats += '\n\tID Number: ' + str(self.id_num)
		turtle_stats += '\n\tBreed: ' + self.breed
		turtle_stats += '\n\tShell Length(ft): ' + str(self.length)
		turtle_stats += '\n\tNumber of Fins: ' + str(self.limbs_num)
		turtle_stats += '\n\tIs endangered: ' + str(self.endangered)
		turtle_stats += '\n\tLast Known Location: ' + str(self.DD_lat) + ', ' + str(self.DD_long)
		turtle_stats += '\n\tHealthy: ' + str(self.healthy)
		return turtle_stats

	# Warning function to alert user if location since last update hasn't changed, will also update healthy status to false
	def warning(self, new_location):
		# Produce a warning if turtle location has not changed since last update
		last_known_location = f'{self.DD_lat}, {self.DD_long}'
		if last_known_location == new_location:
			warning = f'Warning! Turtle({self.id_num}) might be deceased, has not reported movement since last update.'
			setattr(self, 'healthy', False)
		else:
			warning = 'No warnings to report'
		return warning

# Function 1 updates animal's length
def function1(animal_modify, animal_measurement):
	setattr(animal_modify, 'length', animal_measurement)
	return

# Function 2 takes coordinates in decimal degrees of animal's new location and calculates distance traveled since last update/last known location
def function2(lat1, lat2, lon1, lon2):
    # Covert degrees to radians
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    hav_formula = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    distance = 2 * asin(sqrt(hav_formula))
    
    # Radius of earth in miles
    radius_earth = 3956
      
    # Result
    return(distance * radius_earth)

# Function 3 holds dictionaries for shark log and turtle log and stores input from user: new lattitude and longitude 
def function3_shark(id_num, lat2, lon2, date):
	# Location Log for Sharks
	shark_location_log = {12122022: [1, 21.774338, -158.241083]}
	shark_location_log[date] = [lat2, lon2, id_num]
	return shark_location_log.items()

def function3_turtle(id_num, lat2, lon2, date):
	# Location Log for Turtles
	turtle_location_log = {12122022: [1, 21.423201, -157.739575]}
	turtle_location_log[date] = [lat2, lon2, id_num]
	return turtle_location_log.items()

# Function 4 allows user to manually update animal's healthy status
def function4(animal_modify):
	check = ''
	while check != 'yes' and check!= 'no':
		check = input(f"\nIs {getattr(animal_modify, 'breed')} healthy? (yes or no) ")
	if check == 'yes':
		setattr(animal_modify, 'healthy', True)
	else:
		setattr(animal_modify, 'healthy', False)

def main():
	# Variables
	play = ''
	animal_selection = ''
	menu = ''

	# Shark Objects
	shark1 = Shark(1, 'Tiger Shark', 5.25, 'Pacific', 4, 21.774338, -158.241083)
	shark2 = Shark(2, 'Black Tip Shark', 3.75, 'Pacific', 2, 21.285936, -157.855838)

	# Turtle Objects
	turtle3 = Turtle(3, 'Hawksbill Turtle', 2.35, 3, True, 21.423201, -157.739575)
	turtle4 = Turtle(4, 'Green Sea Turtle', 4.25, 4, True, 21.270895, -157.824327)

	# Intro and main loop
	print('Hello and welcome to my Final Exam Project!')
	user_name = input('\nWhat is your name? ')
	while play != 'yes' and play != 'no':
		play_prompt = f'\nOkay {user_name} are you ready to play? I will explain how next. (yes or no) '
		play = input(play_prompt).lower()
	
	if play == 'yes':
		# Print animals
		print(shark1)
		print(shark2)
		print(turtle3)
		print(turtle4)

	while play != 'no':
		# If play is 'yes' assign animal_selection to animal_modify/animal object variable
		if play == 'yes':
			while animal_selection != '1' and animal_selection != '2' and animal_selection != '3' and animal_selection != '4' and animal_selection != '0':
				animal_selection = input('\nSelect an animal: (1, 2, 3, or 4. 0 to quit) ')
			animal_selection = int(animal_selection)
			if animal_selection == 1:
				animal_modify = shark1
			elif animal_selection == 2:
				animal_modify = shark2
			elif animal_selection == 3:
				animal_modify = turtle3
			elif animal_selection == 4:
				animal_modify = turtle4
			else:
				break
			# Print animal selected to modify
			print(animal_modify)
			
			# Loop to access menu functions
			while menu != '1' and menu != '2' and menu != '3' and menu != '4' and menu != '0':
				menu = input(f'\n{user_name}, Let\'s get started! I can perform a few operations.\n  Which operation do you want to perform?\n  1: Update animal measurements.\n  2: Update animal\'s new location and distance traveled.\n  3: Update animal\'s location log.\n  4: Update healthy status.\n  (type the number or 0 to quit) ')
			menu = int(menu)
			if menu == 1:
				# Take input from user (ft) and update animal's length
				animal_measurement = input('\nWhat\'s the new measurment? (feet to 2 decimals) ')
				function1(animal_modify, animal_measurement)
				print(f"\n{getattr(animal_modify, 'breed')}, ID#: {getattr(animal_modify, 'id_num')} is updated to {getattr(animal_modify, 'length')}ft.")
			elif menu == 2:
				# Take input from user, calculate animal's distance traveled since last update/last known location
				lat1 = getattr(animal_modify, 'DD_lat')
				lon1 = getattr(animal_modify, 'DD_long')
				lat2 = float(input('Current Lattitude: (Decimal Degrees to 6 decimals) '))
				lon2 = float(input('Current Longitude: (Decimal Degrees to 6 decimals) '))
				distance_traveled = function2(lat1, lat2, lon1, lon2)
				print(f"\nThe {getattr(animal_modify, 'breed')} traveled: {distance_traveled:.2f} miles since last update.")
				new_location = f'{lat2}, {lon2}'
				print(animal_modify.warning(new_location))
			elif menu == 3:
				# Take input from user and update dictionary of animal log with new coordinates
				if animal_selection == 1 or animal_selection == 2:
					date = int(input('Enter today\'s date: (Format MMDDYYYY) '))
					id_num = int(input('Shark ID Number: (ex. 1) '))
					lat2 = float(input('Current Lattitude: (Decimal Degrees to 6 decimals) '))
					lon2 = float(input('Current Longitude: (Decimal Degrees to 6 decimals) '))
					print(function3_shark(id_num, lat2, lon2, date))
				else:
					date = int(input('Enter today\'s date: (Format MMDDYYYY) '))
					id_num = int(input('Turtle ID Number: (ex. 1) '))
					lat2 = float(input('Current Lattitude: (Decimal Degrees to 6 decimals) '))
					lon2 = float(input('Current Longitude: (Decimal Degrees to 6 decimals) '))
					print(function3_turtle(id_num, lat2, lon2, date))
			elif menu == 4:
				function4(animal_modify)
				print(animal_modify)
			else:
				play = 'no'
		# If play doesn't equal yes or no ask again
		else:
			play = input('\nThat\'s not a response I understand try again? (yes or no)')

	# User entered no or 0 to quit
	print(f'\n{user_name}, Thank\'s for playing! Goodbye.')

main()

