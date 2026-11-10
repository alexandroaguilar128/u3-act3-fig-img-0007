import numpy as np
import pandas as pd
import cv2 
import matplotlib.pyplot as plt

# Alexandro Aguilar NC 0007
print("Alexandro Aguilar NC 0007")
print("UIII Act3 colocar puntos en una imagen en blanco y negro")
mi_imagen = cv2.imread('fugene3.jpg')
plt.imshow(mi_imagen)
plt.title('Album Y Alexandro Aguilar 0007')
plt.show()
print("-+-+-+-+-+-+ Puntos en la imagen -+-+-+-+-+-+")
plt.imshow(mi_imagen)
x = [225,185,265,300]
y = [150,200,200,230]
plt.scatter(x,y, s=20,c='blue')
plt.show()
