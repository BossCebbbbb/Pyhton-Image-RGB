print("hello world")


import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io

from copy import deepcopy


image1 = io.imread("image/01.jpg")

red_channel = deepcopy(image1)
green_channel = deepcopy(image1)
blue_channel = deepcopy(image1)

green_channel[:,:,1]=0
green_channel[:,:,2]=0

blue_channel[:,:,1]=0
blue_channel[:,:,2]=0

fig, ax = plt.subplots(ncols=2, nrows = 2)

ax[0,0].imshow(image1)
ax[0,0].set_title('Original')

ax[0,1].imshow(red_channel)
ax[0,1].set_title('red channel')

ax[1,0].imshow(green_channel)
ax[1,0].set_title('green channel')

ax[1,1].imshow(blue_channel)
ax[1,1].set_title('blue channel')

plt.show()