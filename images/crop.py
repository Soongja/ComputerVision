from PIL import Image

img = Image.open('hand.png')
img = img.crop((200, 170, 290, 260))
img.save('palm.png')