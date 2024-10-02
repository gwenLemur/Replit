import random
import matplotlib.pyplot as plt
import os.path
import numpy as np  # “as” lets us use standard abbreviations
import colorsys
'''Read the image data'''
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'cat.jpg')
original = plt.imread(filename)

# takes the read-only version of the image and makes a copy that can be written to
img = np.array(original, copy=True)
img.setflags(write=True)

height = len(img)
width = len(img[0])




''' Filter Functions '''
def darken(pixel, amount):
    r = int(pixel[0])
    g = int(pixel[1])
    b = int(pixel[2])
    r -= amount
    g -= amount
    b -= amount
    # prevent negative numbers
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    # return the new pixel
    return [r, g, b]


def brighten(pixel, amount):
    r = int(pixel[0])
    g = int(pixel[1])
    b = int(pixel[2])
    r += amount
    g += amount
    b += amount
    # prevent negative numbers
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    # return the new pixel
    return [r, g, b]

def redden(pixel, amount):
    r = int(pixel[0])
    g = int(pixel[1])
    b = int(pixel[2])
    r += amount
    if r > 255:
        r = 255
    return [r, g, b]

def blueify(pixel, amount):
    r = int(pixel[0])
    g = int(pixel[1])
    b = int(pixel[2])
    b += amount
    if b > 255:
        b = 255
    return [r, g, b]

def greyscale(pixel):
    r = int(pixel[0])
    g = int(pixel[1])
    b = int(pixel[2])
    r = (r+g+b) / 3
    g = (r+g+b) / 3
    b = (r+g+b) / 3
    return [r, g, b]


def lumin(pixel):
    r = int(pixel[0])
    g = int(pixel[1])
    b = int(pixel[2])
    hue = 0.21*r + 0.72*g + 0.07*b
    r = hue
    g = hue
    b = hue
    return [r, g, b]


def blend(pixel, color):
    r = int(pixel[0])
    g = int(pixel[1])
    b = int(pixel[2])
    r = (r + color[0]) / 2
    g = (g + color[1]) / 2
    b = (b + color[2]) / 2
    return [r, g, b]

def invert(pixel):
    r = int(pixel[0])
    g = int(pixel[1])
    b = int(pixel[2])
    r = 255 - r
    g = 255 - g
    b = 255 - b
    return [r, g, b]

def sepia(pixel):
    r = int(pixel[0])
    g = int(pixel[1])
    b = int(pixel[2])
    r = 0.393*r + 0.769*g + 0.189*b
    g = 0.349*r + 0.686*g + 0.168*b
    b = 0.272*r + 0.534*g + 0.131*b

    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    # return the new pixel
    return [r, g, b]


def desaturate(pixel):
    r = int(pixel[0]) / 255
    g = int(pixel[0]) / 255
    b = int(pixel[0]) / 255
    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    s *= 2

    if s < 1:
        s = 1

    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return [int(r*255), int(g*255), int(b*255)]


def ran(pixel):
    r = int(pixel[0])
    g = int(pixel[1])
    b = int(pixel[2])
    r += random.randint(-100, 100)
    g += random.randint(-100, 100)
    b += random.randint(-100, 100)
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    return [r, g, b]


for row in range(height):
    for col in range(width):
        img[row][col] = invert(img[row][col])

'''Show the image data'''
fig, ax = plt.subplots(1, 2)
ax[0].title.set_text("Original")
ax[0].imshow(original, interpolation='none')
ax[1].title.set_text("Random")
ax[1].imshow(img, interpolation='none')
fig.show()
plt.show()
