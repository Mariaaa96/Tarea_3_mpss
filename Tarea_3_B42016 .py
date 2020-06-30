#!/usr/bin/env python
# coding: utf-8

# In[72]:


###### import numpy as np
import pandas as pd
import os
import math
import numpy as np 
from scipy.optimize import curve_fit
import csv
from scipy.stats import norm
import matplotlib.mlab as mlab
import scipy
from scipy import stats 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d



# Encontrar la mejor curva de ajuste para las funciones de densidad marginales de X y Y.
# Se hace un vector de los valores de "x" y "y".
x1=np.linspace(5,15,11) 

y1=np.linspace(5,25,21)

    #Se abre el archivo
valores = pd.read_csv("xy.csv")

#Se construye las funciones marginales de X y Y
fX=np.sum(valores, axis = 1)
fY=np.sum(valores, axis = 0) 
print("En las gráficas colocadas en la parte 4, se observa que ambas funciones se comportan como gaussianas. Por lo que se determinará su ajuste mediante curve_fit.")

#Se inicializa el .csv
xyp = pd.read_csv('xyp.csv')
#Se obtiene una lista de los valores de x, y y p
xs=xyp.loc[:,"x"] 
ys=xyp.loc[:,"y"] 
ps=xyp.loc[:,"p"] 
#Se obtiene la media, la desviación estándar y varianza de x
mediax=xs.mean() 
stdx=xs.std()
varianzax = stdx**2
#Se obtiene la media, desviación estándar y varianza de y
mediay=ys.mean()
stdy=ys.std()
varianzay = stdy**2

#Se define la distribución gaussiana
def gaussiana(x, mu, a, de):
    return a * np.exp(-((x-mu)**2)/(2*(de**2)))

#Se compara con los valores de los parámetros obtenidos previamente
print()
param1, _=curve_fit(gaussiana, x1,fX)
ax = 1/math.sqrt(2*np.pi*(stdx**2))
print('Se tiene que la media, la amplitud y la desviación estándar son ', mediax, ax, stdx, ',respectivamente. Esto se compara a lo siguiente:')
print(param1)
print('Como se observa, se acerca bastante, exceptuando la desviación estándar, la cual es ligeramente mayor.')
print()
param2,_=curve_fit(gaussiana, y1,fY[1:22])
ay = 1/math.sqrt(2*np.pi*stdy**2)
print('Se tiene que la media, la amplitud y la desviación estándar son ', mediay, ay, stdy, ',respectivamente. Esto se compara a lo siguiente:')
print(param2)
print('Como se observa, se acerca bastante, exceptuando la desviación estándar, la cual es ligeramente mayor.')
print()
print('Se concluye que realmente se puede modelar como una distribución gaussiana.')    


# In[81]:


'''2 Función de densidad conjunta: Al asumir que hay independencia, 
se dice que ésta es la multiplicación de las  funciones marginales.
. Se va a trabajar con xyp.csv'''
#Se inicializa el .csv
xyp = pd.read_csv('xyp.csv')
#Se obtiene una lista de los valores de x, y y p
xs=xyp.loc[:,"x"] 
ys=xyp.loc[:,"y"] 
ps=xyp.loc[:,"p"] 

yy1=np.linspace(5,15,11) 
print('Para obtener la función de densidad conjunta, se debe multiplicar ambas funciones marginales. Lo cual se puede ver de la siguiente manera si se definen los rangos de la misma longitud:')
def conjunta (x,y, mux, muy,aax,aay, dex,dey):
    return aax*aay* np.exp((-((x-mux)**2)/(2*(dex**2)))+(-((y-muy)**2)/(2*(dex**2))))
print(conjunta(x1,yy1, mediax,mediay,a1,ay,stdx,stdy))


# In[74]:


#Correlación: Se plantea que es la sumatoria de la multiplicación de los valores de x, y y su probabilidad conjunta 

#Se multiplica los elementos de los arreglos
multCorr=xs*ys*ps
#Se suma el nuevo arreglo para obtener la correlación
correlacion=np.sum(multCorr)
print("La correlación es: ", correlacion)

#Covarianza: Consiste en la sumatoria de la multiplicación de los valores de x y y menos su media, por su probailidad conjunta

#Se obtiene la diferencia entre los valores x, y, y sus medias
difx=xs-mediax
dify=ys-mediay
#Se multiplica los elementos de los arreglos
multCov=difx*dify*ps
covarianza=np.sum(multCov)
print("La covarianza es: ", covarianza)

#Coeficiente de correlación: Es la covarianza entre la multiplicación de las desviaciones estándar

coefCorrelacion=covarianza/(stdx*stdy)
print("El coeficiente de correlación es: ", coefCorrelacion)


# In[78]:


#Gráfica de las funciones marginales
 
plt.plot(x1, fX)
plt.title("Probabilidades")
plt.xlabel("Datos")
plt.ylabel("Probabilidad")
plt.show()

plt.plot(y1, fY[1:22])
plt.title("Probabilidades")
plt.xlabel("Datos")
plt.ylabel("Probabilidad")
plt.show()





#Gráfica en 3D de los datos
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(xs, ys, ps, c=ps, cmap='hot');


# In[ ]:




