"""
Example: create a small collage

More on Pillow on 
http://pillow.readthedocs.io/en/5.2.x/handbook/index.html
"""

from PIL import Image, ImageDraw, ImageFont

# read images
logo = Image.open('python_logo.png')
brain = Image.open('brain.png')    

# paste to empty image
img = Image.new('RGBA', (800, 500), "white")    
logo = logo.resize((150, 150))
img.paste(logo, (100, 140))
img.paste(brain, (500, 100))    

# create arrow
arrow = Image.new('RGBA', (200, 200), "white")
draw = ImageDraw.Draw(arrow)
draw.rectangle((0, 50, 100, 100), fill="#ff6900") # x-position, y-position, x-size, y-size
draw.polygon((100, 25, 100, 125, 150, 75), fill="#ff6900")# x-position, y-position, x-size, y-size, x-dimension, y-dimension
img.paste(arrow, (325, 150))

# add text
draw = ImageDraw.Draw(img)
arial = ImageFont.truetype('arial.ttf', 40) # font filename, size
draw.text((202, 360), "Python rocks your brain!", fill='#6e0096', font=arial)

# save final picture
img.save('rocks.png')
img.show()
