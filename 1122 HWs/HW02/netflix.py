'''
Jimmy Lauchoy
CS1122
'''
from PIL import Image, ImageDraw
import random
colors = ["black","green","blue","red","pink","purple","violet","orange"]
randomIndex = random.randint(0,len(colors)-1)
randomColor = colors[randomIndex]

im = Image.new("RGB", (230,275), (255,255,255))
draw = ImageDraw.Draw(im)
draw.rectangle(((15,15),(215,215)), fill = randomColor)
draw.ellipse(((45,45),(80,80)), fill = "white")
draw.ellipse(((145,45),(180,80)), fill = "white")
draw.arc(((65,145),(160,180)),45, 135, fill = "white")
draw.text((80, 235),"Jimmy Lauchoy",(0,0,0))
im.save("netflix_logo.png")