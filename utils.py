import random
from matplotlib.colors import LinearSegmentedColormap, rgb2hex
import numpy as np


def shuffle(arr):
    shuffled = []
    while len(arr) > 0:
        rand_int = random.randrange(0, len(arr))
        shuffled.append(arr[rand_int])
        arr.pop(rand_int)
    return shuffled

def equal(amount_cells, amount_cars):
    mean_distance = amount_cells / amount_cars
    new_arr = []
    for i in range(amount_cars):
        new_pos = round(i * mean_distance)
        new_arr.append(new_pos)
    return new_arr

def get_random_array(x):
    return shuffle([i for i in range(x)])

def generate_gradient_rgbs(num_buckets):
    rgb_codes = []
    step_size = 1024 / num_buckets
    for step in range(0,num_buckets):
        red = int(max(0, 255 - (step_size*step*0.5))) # step size is half of the step size since both this item goes down and the next one goes up
        blue = int(max(0, 255 - (step_size*0.5*(num_buckets-step-1))))
        green = (255 - red) if red else (255 - blue)
        rgb_codes.append((red, green, blue))
    return rgb_codes

def get_new_color_array(v_max):
    colors = [(1, 0, 0), (1, 0.5, 0), (1, 1, 0), (0.4, 0.8, 0), (0, 0.6, 0)]
    cm = LinearSegmentedColormap.from_list("Custom", colors, N=v_max+1)
    color_list = [rgb2hex(cm(i)) for i in range(cm.N)]
    return color_list
    # mat = np.indices((10,10))[1]      # uncomment to view gradient
    # plt.imshow(mat, cmap=cm)
    # plt.show()


