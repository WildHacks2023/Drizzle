import time
import math
import datetime
import random
import tkinter as tk
import project_utilities

####STORING USER DATA####

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
gallons_of_water = 0
drops_of_water = 0



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

####MENU####
def print_menu():
    print('''
---------------------------------------------------------------------
Welcome to Drizzle!

Settings / Browse Options
---------------------------------------------------------------------
1 - Start Shower
2 - See how many drops you've saved
3 - Leave
---------------------------------------------------------------------
     ''')

####CALCULATING THE AMMOUNT OF WATER SAVED IN GALLONS####
normal=2.5
WaterSense = 2.0


def water_saved_in_gallons(time, showerhead_type=normal):
  time = timer()
  num_minutes = time/60
  num_spent = goal - num_minutes
  gallons_saved_or_lost = round(num_spent*showerhead_type, 2)
  print("You spent ", round(num_minutes, 1), "minutes in the shower.")
  drops_of_water = drops_of_water + gallons_saved_or_lost*15140
  if gallons_saved_or_lost > 0:
    print("You saved", drops_of_water, "gallons of water!")
    return drops_of_water
  else:
    print("You used", drops_of_water, "gallons more than the goal.")
    return drops_of_water

####STOPWATCH FEATURE####
#This is the part of the feature with the stopwatch

  
def timer(sec):
   mins = sec / 60
   sec = sec % 60
   hours = mins / 60
   mins = mins % 60
   final_time = "{0}:{1}:{2}".format(int(hours),int(mins),sec)
   input("Press Enter to start shower")
   start_time = time.time()
   input("Press Enter to stop")
   end_time = time.time()
   time_lapsed = end_time - start_time
#
   print("Time Lapsed =", final_time)
   if time_lapsed < goal:
      print("You met the shower goal!")
   water_saved_in_gallons(time_lapsed)
   return time_lapsed
MOUSE_CLICK = '<Button-1>'




####FISH GENERATION####

list_of_colors = ['alice blue', 'antique white', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanched almond', 'blue', 'blue violet', 'brown', 'burlywood', 'cadet blue', 'chartreuse', 'chocolate', 'coral', 'cornflower blue', 'cornsilk', 'crimson', 'cyan', 'dark blue', 'dark cyan', 'dark goldenrod', 'dark gray', 'dark grey', 'dark green', 'dark khaki', 'dark magenta', 'dark olive green', 'dark orange', 'dark orchid', 'dark red', 'dark salmon', 'dark sea green', 'dark slate blue', 'dark slate gray', 'dark slate grey', 'dark turquoise', 'dark violet', 'deep pink', 'deep sky blue', 'dim gray', 'dim grey', 'dodger blue', 'firebrick', 'floral white', 'forest green', 'gainsboro', 'ghost white', 'gold', 'goldenrod', 'gray', 'grey', 'green', 'green yellow', 'honeydew', 'hot pink', 'indian red', 'ivory', 'khaki', 'lavender', 'lavender blush', 'lawn green', 'lemon chiffon', 'light blue', 'light coral', 'light cyan', 'light goldenrod yellow', 'light gray', 'light grey', 'light green', 'light pink', 'light salmon', 'light sea green', 'light sky blue', 'light slate gray', 'light slate grey', 'light steel blue', 'light yellow', 'lime green', 'linen', 'magenta', 'maroon', 'medium aquamarine', 'medium blue', 'medium orchid', 'medium purple', 'medium sea green', 'medium slate blue', 'medium spring green', 'medium turquoise', 'medium violet red', 'midnight blue', 'mint cream', 'misty rose', 'moccasin', 'navajo white', 'navy', 'old lace', 'olive', 'olive drab', 'orange', 'orange red', 'orchid', 'pale goldenrod', 'pale green', 'pale turquoise', 'pale violet red', 'papaya whip', 'peach puff', 'peru', 'pink', 'plum', 'powder blue', 'purple', 'red', 'rosy brown', 'royal blue', 'saddle brown', 'salmon', 'sandy brown', 'sea green', 'seashell', 'sienna', 'silver', 'sky blue', 'slate blue', 'slate gray', 'slate grey', 'snow', 'spring green', 'steel blue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'white smoke', 'yellow', 'yellow green']

def make_oval(the_canvas, center_x, center_y, radius_x, radius_y, color="brown", tag="", outline="black"):
    the_canvas.create_oval(
        center_x - radius_x, center_y + radius_y, #bottom left-coordinate
        center_x + radius_x, center_y - radius_y, #top right-coordinate
        fill=color, tags=tag, outline=outline)


def make_fish(a_canvas, center, size=50, color="blue", tag=""):
    x = center[0]
    y = center[1]
    # Draw the body of the fish
    size = random.randint(15, 100)
    a_canvas.create_polygon(
       x - (2/3)*size, y,
       x, y+(1/2)*size,
       x + size*1.5, y,
       x, y-(1/2)*size, 
       width=2,
       fill=random.choice(list_of_colors),
       smooth=True, tag="")
    # Draw the tail of the fish
    a_canvas.create_polygon(x + size, y,
                          x + size*1.6, y+size/2,
                          x + size*1.6, y-size/2,
                           fill=random.choice(list_of_colors), outline="", 
                           smooth=True, tag="")

    # Draw the eye of the fish
    make_oval(a_canvas, x, y - size/5, size*(1/8), size*(1/8), color=random.choice(list_of_colors), outline="",
              tag="")

    # Draw the pupil of the eye
    make_oval(a_canvas, x- size*(1/15), y - size/4.7, size*(1/20), size*(1/20), color="white", outline="",
              tag="")

#def make_shark(a_canvas, center, size = 100, color="grey", tag=""):
   #main body


### Example usage for fish
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

make_fish(canvas, (50, 50,), tag="fish1")
make_fish(canvas, (150, 150), tag="fish2")

####ANIMATING FISH####
##Move in circle

###PROGRAM####
while True:
   print_menu()
   choice = input("What would you like to do? Select 1, 2 or 3 ")
   if choice == "1":
      timer()
   elif choice == "2":
      if gallons_of_water > 0:
         print("Amazing, you have saved", drops_of_water, "drops of water!")
      elif gallons_of_water <= 0:
        print("Hm, seems like you have used", (-1*drops_of_water), "drops above the goal. You can do better!")
   elif choice == "3":
      print("Quiting...")
      break
   else:
        print(choice, "is an invalid choice. Please try again.")
        print()
   input("Press enter to continue...")
      


root.mainloop()
