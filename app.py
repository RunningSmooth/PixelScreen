import numpy, pyautogui
import matplotlib.pyplot as plt
from matplotlib import animation
import time

screen_size = (1920, 1080)

# common divisors for screen-size (1980, 1080): 
# 1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120
square_side_length = 8
square_num_x = int(1080 / square_side_length)
square_num_y = int(1920 / square_side_length)

numpy_frame = pyautogui.screenshot()
fig = plt.figure()
im = plt.imshow(numpy_frame)

def animate(i):
    start = time.perf_counter()
    img = pyautogui.screenshot()
    numpy_frame = numpy.asarray(img)

    k = 0
    part_array = numpy.empty([square_num_x, square_num_y, 3])
    for i in range(square_num_x):
        for j in range(square_num_y):
            temp = numpy.round(numpy.mean(numpy_frame[i*square_side_length:(i+1)*square_side_length, j*square_side_length:(j+1)*square_side_length], axis=(0, 1)))
            part_array[i, j] = temp
    
    # Insert mean
    for r in range(square_num_x):
        for k in range(square_num_y):
            numpy_frame[r*square_side_length:(r+1)*square_side_length, k*square_side_length:(k+1)*square_side_length] = part_array[r, k]

    plt.clf()
    plt.imshow(numpy_frame)
    end = time.perf_counter()
    print("Time: " ,end - start, "Seconds")

anim = animation.FuncAnimation(fig, animate,
                               frames=60)

plt.show()
