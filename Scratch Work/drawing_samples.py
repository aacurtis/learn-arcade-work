"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.

Multi-line comments are surrounded by three double-quote marks.
Single-line comments start with a hash/pound sign. #
"""

# Import the arcade library 
import arcade

# Open up a window
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# The drawing code will go here
arcade.draw_arc_outline(center_x = 300, center_y=340, width=60, height=100, color=arcade.csscolor.BLACK, start_angle=0, end_angle=180, border_width=3, tilt_angle=45)

# Finish drawing
arcade.finish_render()
# Keep the window up until someone closes it. 
arcade.run()

