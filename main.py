import turtle
import tkinter as tk
import math
import time




def draw_inscribed_shape(number_of_sides):
   t.pencolor("yellow")
   angle = 360 / number_of_sides
   angle = math.radians(angle)
   adding_angle = angle
   t.penup()
   count = 0
   while count <= number_of_sides:
       x_position = 150 * math.cos(angle)
       y_position = 150 * math.sin(angle) + 80
       t.goto(x_position, y_position)
       t.pendown()
       angle = angle + adding_angle
       count = count + 1
   t.penup()




def draw_circumscribed_shape(number_of_sides):
   t.pencolor("cyan")
   angle = 360 / number_of_sides
   angle = math.radians(angle)
   adding_angle = angle
   max_length_from_radius = 150 / math.cos(angle / 2)


   count = 0
   while count <= number_of_sides:
       x_position = max_length_from_radius * math.cos(angle)
       y_position = max_length_from_radius * math.sin(angle) +80
       t.goto(x_position, y_position)
       t.pendown()
       angle = angle + adding_angle
       count = count + 1


   t.penup()




def draw_shapes():
   t.clear()
   tk.Label(root,
            text=("                                                                                               "),
            bg="#111111", fg="#111111", font=("Arial", "30")).place(
       x=400, y=675)
   t.hideturtle()
   input_value = int(text_box.get("1.0", tk.END))
   number_of_sides = input_value


   if number_of_sides >= 3:
       tk.Label(root, text="                                                                  ", bg="#111111", fg="#111111",
font=("Arial", "24")).place(x=350, y=800)
       # draws circle function
       t.speed(0)
       t.color("red")
       radius = 150
       t.penup()
       t.goto(0, 80 - radius)  # Move the turtle to the bottom center of the circle
       t.pendown()
       t.circle(radius)  # Draw the circle
       t.speed(4)
       draw_inscribed_shape(number_of_sides)
       draw_circumscribed_shape(number_of_sides)
       t.penup()


       # step 1: define radius
       radius = 1


       # Step 2, finds the interior angle in radians
       angle = 360 / number_of_sides
       angle = math.radians(angle)


       # Cosine law to find c
       c = math.sqrt(2 - 2 * math.cos(angle))


       # Pythagorean theorem to find the height h
       h = math.sqrt(1 - (c / 2) ** 2)


       # area of one of the n triangles
       area_abc = c * h / 2


       # total inscribed area = area_abc times number of sides
       inscribed_area = area_abc * number_of_sides


       print(inscribed_area)


       # circumscribed area
       e = 1 / math.cos(angle / 2)
       f = math.sqrt(2 * e * e - 2 * e * e * math.cos(angle))


       area_def = f / 2
       circumscribed_area = number_of_sides * area_def


       print(circumscribed_area)
       tk.Label(root, text= (f"{round(inscribed_area,8)} < π < {round(circumscribed_area,8)}"), bg="#111111", fg="lawngreen", font=("Arial", "30")).place(
           x=400, y=675)


   else:
       tk.Label(root, text="Your number must be 3 or greater. ", bg="#111111", fg="red", font=("Arial", "24")).place(x=350, y=800)






# Create a tkinter window
root = tk.Tk()
root.title("PIdentity")


# Create a turtle canvas
canvas = tk.Canvas(root, width=1200, height=1000)
canvas.pack()


# Create a turtle screen
screen = turtle.TurtleScreen(canvas)


# Create a turtle object
t = turtle.RawTurtle(screen)


calculate_button = tk.Button(root, text="Calculate", command=draw_shapes, font=("Arial", "24"))
calculate_button.place(x=675, y=750)
time.sleep(0.5)


# Text box
text_box = tk.Text(root, height=1, width=4, bg="white", fg="black", font=("Arial", 24))
text_box.place(x=575, y=750)


tk.Label(root, text="Number of Sides: ", bg="#111111", fg="white", font=("Arial", "24")).place(x=350, y=750)
screen.bgcolor("#111111")


tk.Label(root, text="PIdentity", bg="#111111", fg="white", font=("Arial", "36", "bold")).place(x=530, y=50)


# Run the tkinter event loop
tk.mainloop()
