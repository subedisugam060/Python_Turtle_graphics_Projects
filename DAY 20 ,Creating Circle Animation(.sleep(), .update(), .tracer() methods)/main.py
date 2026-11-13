import turtle
import time

screen = turtle.Screen()
#screen.tracer(0)  # Turn off automatic updates

# Drawing code here
# ...
for _ in range(36):
    turtle.forward(10)
    turtle.right(10)
    #screen.update()  # Manually update the screen
    #time.sleep(0.1)  # Pause for 0.1 seconds

screen.mainloop()  # Keep the window open
