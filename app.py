import numpy, pyautogui
import matplotlib.pyplot as plt
from matplotlib import animation
from PIL import Image
import time

screen_size = (1920, 1080)
square_num_x = 9
square_num_y = 16
len_x = int(1080 / square_num_x)
len_y = int(1920 / square_num_y)

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
            temp = numpy.round(numpy.mean(numpy_frame[i*len_x:(i+1)*len_x, j*len_y:(j+1)*len_y], axis=(0, 1)))
            part_array[i, j] = temp

    for r in range(square_num_x):
        for k in range(square_num_y):
            for i in range(r*len_x, (r+1)*len_x):
                for j in range(k*len_y, (k+1)*len_y):
                    numpy_frame[i, j] = part_array[r][k]
    plt.clf()
    plt.imshow(numpy_frame)
    end = time.perf_counter()
    print(end - start)

anim = animation.FuncAnimation(fig, animate,
                               interval=100)

plt.show()