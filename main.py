# Import modules
import tkinter as tk
import math
import datetime
import screeninfo
import random

# Get the display size
monitor = screeninfo.get_monitors()[0]
WINDOW_WIDTH = monitor.width
WINDOW_HEIGHT = monitor.height

# Define constants
SUN_RADIUS = WINDOW_WIDTH // 50
SUN_COLOR = "yellow"
PLANETS = [
    {"name": "Mercury", "radius": WINDOW_WIDTH // 250, "color": "gray", "distance": WINDOW_WIDTH // 35, "speed": 4.74},
    {"name": "Venus", "radius": WINDOW_WIDTH // 125, "color": "orange", "distance": WINDOW_WIDTH // 23, "speed": 3.5},
    {"name": "Earth", "radius": WINDOW_WIDTH // 125, "color": "blue", "distance": WINDOW_WIDTH // 17, "speed": 2.98},
    {"name": "Mars", "radius": WINDOW_WIDTH // 180, "color": "red", "distance": WINDOW_WIDTH // 13, "speed": 2.41},
    {"name": "Jupiter", "radius": WINDOW_WIDTH // 62, "color": "brown", "distance": WINDOW_WIDTH // 9, "speed": 1.31},
    {"name": "Saturn", "radius": WINDOW_WIDTH // 83, "color": "gold", "distance": WINDOW_WIDTH // 7, "speed": 0.97},
    {"name": "Uranus", "radius": WINDOW_WIDTH // 104, "color": "lightblue", "distance": WINDOW_WIDTH // 6, "speed": 0.68},
    {"name": "Neptune", "radius": WINDOW_WIDTH // 104, "color": "purple", "distance": WINDOW_WIDTH // 5, "speed": 0.54},
]
TIME_FACTOR = 1 # The factor by which the simulation time is faster than real time
SIMULATION_DATE = datetime.date(2021, 1, 1) # The initial date of the simulation

# Define functions
def draw_sun():
    # Draw the sun on the canvas
    canvas.create_oval(WINDOW_WIDTH / 2 - SUN_RADIUS, WINDOW_HEIGHT / 2 - SUN_RADIUS,
                       WINDOW_WIDTH / 2 + SUN_RADIUS, WINDOW_HEIGHT / 2 + SUN_RADIUS,
                       fill=SUN_COLOR)

def draw_planets():
    # Draw the planets and their orbits on the canvas
    global PLANETS, SIMULATION_DATE
    for planet in PLANETS:
        # Calculate the x and y coordinates of the planet based on its distance and angle from the sun
        x = WINDOW_WIDTH / 2 + planet["distance"] * math.cos(math.radians(planet["angle"]))
        y = WINDOW_HEIGHT / 2 + planet["distance"] * math.sin(math.radians(planet["angle"]))
        # Draw the orbit as a circle on the canvas
        canvas.create_oval(WINDOW_WIDTH / 2 - planet["distance"], WINDOW_HEIGHT / 2 - planet["distance"],
                           WINDOW_WIDTH / 2 + planet["distance"], WINDOW_HEIGHT / 2 + planet["distance"],
                           outline="white")
        # Draw the planet as a circle on the canvas
        canvas.create_oval(x - planet["radius"], y - planet["radius"],
                           x + planet["radius"], y + planet["radius"],
                           fill=planet["color"])
        # Update the angle of the planet for the next frame
        planet["angle"] += planet["speed"] * TIME_FACTOR
    # Update the simulation date for the next frame
    SIMULATION_DATE += datetime.timedelta(days=TIME_FACTOR)

def draw_date():
    # Draw the simulation date on the canvas
    global SIMULATION_DATE
    canvas.create_text(WINDOW_WIDTH // 12.5 , WINDOW_HEIGHT // 24 , text=SIMULATION_DATE.strftime("%Y-%m-%d"), font=("Arial", int(WINDOW_HEIGHT /30)), fill="white")

def animate():
    # Animate the solar system by drawing the sun, the planets and the date and scheduling the next animation frame
    canvas.delete(tk.ALL) # Clear the canvas
    draw_sun() # Draw the sun
    draw_planets() # Draw the planets and their orbits
    draw_date() # Draw the simulation date
    root.after(50, animate) # Schedule the next animation frame

def increase_time():
    # Increase the time factor by one and update the label accordingly
    global TIME_FACTOR
    TIME_FACTOR += 1
    time_label.config(text=f"Time: x{TIME_FACTOR}")

def decrease_time():
    # Decrease the time factor by one and update the label accordingly if it is greater than one
    global TIME_FACTOR
    if TIME_FACTOR > 1:
        TIME_FACTOR -= 1
        time_label.config(text=f"Time: x{TIME_FACTOR}")

# Create the root window
root = tk.Tk()
root.title("Solar System")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# Create the canvas widget
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")

# Create the buttons and the label for changing the time factor on the canvas
increase_button = tk.Button(canvas, text="+", command=increase_time)
decrease_button = tk.Button(canvas, text="-", command=decrease_time)
time_label = tk.Label(canvas, text=f"Time: x{TIME_FACTOR}")

# Arrange the widgets using place layout
canvas.place(x=0, y=0)
increase_button.place(x=0, y=0)
decrease_button.place(x=WINDOW_WIDTH // 25, y=0)
time_label.place(x=WINDOW_WIDTH // 12.5, y=0)

# Initialize the angle of each planet to a random value between 0 and 360 degrees
for planet in PLANETS:
    planet["angle"] = math.floor(random.random() * 360)

# Start the animation loop
animate()

# Start the main loop
root.mainloop()
