"""
Create a dice image

More on Pillow on 
http://pillow.readthedocs.io/en/5.2.x/handbook/index.html
"""

from PIL import Image
from PIL import ImageDraw

# create a new image
img = Image.new('RGB', (64,64), '#aa0078')
d = ImageDraw.Draw(img)  # prepares drawing tool

d.ellipse(((26, 26), (38, 38)), 'white')
img.save('dice_one.png')
img.show()
