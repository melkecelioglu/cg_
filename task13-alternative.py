import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Open image and convert to HSV
im = Image.open('PolitechnikaBialostocka.jpg').convert('HSV')

# Get the hue channel and create a mask
Hue = np.array(im.getchannel('H'))
mask = np.zeros_like(Hue, dtype=np.uint8)
mask[(Hue>80) & (Hue<90)] = 1

# Calculate percentage of image covered by green
percent_green = mask.mean() * 100

# Open original image to draw on
img = Image.open('PolitechnikaBialostocka.jpg')
I1 = ImageDraw.Draw(img)

# Use Montserrat-ExtraLight font
myFont = ImageFont.truetype("Montserrat-ExtraLight.ttf", 35)

# Draw text on image
I1.text((20, 50), f"{percent_green:.2f}% is covered by green", font=myFont, fill=(255, 69, 0))

# Show the image
img.show()
