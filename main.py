import cv2
from PIL import Image
from matplotlib import pyplot as plt

i=cv2.imread("scaled.png")
grey=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
cv2.imwrite("grey.png",grey)

im=Image.open("cog.jpeg")
r,g,b=im.split()
img=Image.merge("RGB",(b,r,g))
img.save("rgb.jpeg")

ir=im.rotate(45)
ir.save("rotate.jpeg")
horizontal_flip=im.transpose(Image.FLIP_TOP_BOTTOM)
horizontal_flip.save("flip.jpeg")

j=cv2.imread("grey.png")
gr=cv2.rotate(j,cv2.cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite("BOB.png",gr)

im.thumbnail((420,690))
im.save("t.jpeg")

Nem=cv2.imread("grey.png")

plt.xticks([]),plt.yticks([])
plt.plot([100,200,300],[100,200,300],'c',linewidth=5)
plt.show()