import time
import math
import datetime
import random
import tkinter


####FIRST TIME APP USAGE QUESTIONS####
name = input("What is your name? ")
goal = 8
'''goal = float(input("What is your shower time goal? "))
if goal < 5:
   #Hover
   print("Super Shower Speedster!")
if 5 <= goal <= 6:
   print("Fast n' Furious")
if 6 <= goal <= 7:
   print("YAY")'''




####GREETING UPON OPENING APP####
random_morning_greeting = ["Good morning,", "Welcome,", "Thank you for starting your day by saving a drop for the environment,"]
random_afternoon_greeting = ["Good afternoon,", "Welcome,", "Hope you are having a positive day,"]
random_evening_greeting = ["Good evening,", "Welcome,", "End your day strong,"]
# Get the current time
current_time = datetime.datetime.now().time()
# Get the hour from the current time
hour = current_time.hour
# Greet the user based on the time of day
if hour < 12:
    print(random.choice(random_morning_greeting), name)
elif hour < 18:
    print(random.choice(random_afternoon_greeting), name)
else:
    print(random.choice(random_evening_greeting), name)


####STOPWATCH FEATURE####
#This is the part of the feature with the stopwatch
def time_convert(sec):
  mins = sec / 60
  sec = sec % 60
  hours = mins / 60
  mins = mins % 60
  final_time = "{0}:{1}:{2}".format(int(hours),int(mins),sec)
  return final_time
  

input("Press Enter to start shower")
start_time = time.time()

input("Press Enter to stop")
end_time = time.time()

time_lapsed = end_time - start_time
num_format = time_convert(time_lapsed)
print("Time Lapsed =", num_format)

####CALCULATING THE AMMOUNT OF WATER SAVED IN GALLONS####
normal=2.5
WaterSense = 2.0
def water_saved_in_gallons(time, showerhead_type=normal):
  num_minutes = time/60
  num_spent = goal - num_minutes
  gallons_saved_or_lost = round(num_spent*showerhead_type, 2)
  print("You spent ", round(num_minutes, 1), "minutes in the shower.")
  if gallons_saved_or_lost > 0:
    print("You saved", gallons_saved_or_lost, "gallons of water!")
    return True
  else:
    print("You used", gallons_saved_or_lost, "gallons more than the goal.")
    return False

water_saved_in_gallons(time_lapsed)


####FISH GENERATION####
