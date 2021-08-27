import numpy, pyautogui
import matplotlib.pyplot as plt
from matplotlib import animation
import time

# Setting screen-size.
screen_size = (1920, 1080)

# common divisors for screen-size (1980, 1080): 
# 1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120   -> values for square_side_length
square_side_length = 12

# Calculating how many squares are needed in each axial direction.
square_num_x = int(1920 / square_side_length)
square_num_y = int(1080 / square_side_length)

# Taking first screenshot and adding it to plot.
numpy_frame = pyautogui.screenshot()
plt.rcParams['toolbar'] = 'None'
fig = plt.figure(figsize=(12, 7))
fig.canvas.manager.set_window_title('PixelScreen by RunningSmooth')
im = plt.imshow(numpy_frame)
plt.axis('off')

def animate(i):
    """ Function that takes a screenshot and translates it into an pixel-image. """

    start = time.perf_counter()

    # Takes screenshot and translates it into a numpy 3d-Array.
    img = pyautogui.screenshot()
    numpy_frame = numpy.asarray(img)

    # Takes squares out of the picture. Calculates and saves the mean-values of their colors in an 3d-Array.
    part_array = numpy.empty([square_num_y, square_num_x, 3])
    for i in range(square_num_y):
        for j in range(square_num_x):
            temp = numpy.round(numpy.mean(numpy_frame[i*square_side_length:(i+1)*square_side_length, j*square_side_length:(j+1)*square_side_length], axis=(0, 1)))
            part_array[i, j] = temp
    
    # Insert mean-values from the before created 3d Array into the picture array.
    for r in range(square_num_y):
        for k in range(square_num_x):
            numpy_frame[r*square_side_length:(r+1)*square_side_length, k*square_side_length:(k+1)*square_side_length] = part_array[r, k]

    # Clears plot and plots the image with the mean values.
    plt.clf()
    plt.imshow(numpy_frame)
    plt.axis('off')

    end = time.perf_counter()
    print("Time: " ,end - start, "Seconds")

# Setting an animation for the plot.
anim = animation.FuncAnimation(fig, animate,
                               frames=60)

# Show plot.
plt.show()
