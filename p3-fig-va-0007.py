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
print("-+-+-+-+-+-+ Cuadro en la imagen -+-+-+-+-+-+")
mi_imagen = cv2.imread('fugene3.jpg')
plt.imshow(mi_imagen)
x = [100,100,345,345,100]
y = [350,100,100,350,350]
# Nuevas coordenadas del cuadro
x = [valor * 0.75 for valor in x]
y = [valor * 0.75 for valor in y]
x = [valor + 50 for valor in x]
plt.plot(x,y, c='red')
plt.show()
print("-+-+-+-+-+-+ Circulo verde en la imagen -+-+-+-+-+-+")
mi_imagen = cv2.imread('fugene3.jpg')
plt.imshow(mi_imagen)
N = 30 # lado del poligono
x = np.zeros((N+1),)
y = np.zeros((N+1),)
(xc,yc) = (220,220)
r = 150 # radio
for mi_imagen in range(N+1):
    t = 2*np.pi/N*mi_imagen
    x[mi_imagen] = xc + r*np.cos(t)
    y[mi_imagen] = yc + r*np.sin(t)
plt.plot(x, y, c='green')
plt.show()
print("Alexandro Aguilar NC 0007")