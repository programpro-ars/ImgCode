from PIL import Image
import random

def get_bin(c):
    result = "{0:b}".format(ord(c))
    return ("0" * (18 - len(result))) + result

img = Image.open("source/img.jpg")
img = img.convert("RGBA")
pixels = img.load()
s = 0
with open('source/Input_Text.txt', 'r') as inp_file:
    data = inp_file.read()
    bin_representation = ''
    for i in range(len(data)):
        x = get_bin(data[i])
        bin_representation += x

ind = 0
max_size = len(bin_representation)
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if (ind < max_size):
            pixels[i, j] = (pixels[i, j][0], pixels[i, j][1], pixels[i, j][2], 255 - int(bin_representation[ind]))
        elif (ind == max_size):
            pixels[i, j] = (pixels[i, j][0], pixels[i, j][1], pixels[i, j][2], 253)
        else:
            pixels[i, j] = (pixels[i, j][0], pixels[i, j][1], pixels[i, j][2], random.randint(254, 255))
        ind += 1
img.save("source/output.png")
