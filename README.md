# Universidad de Costa Rica
# Escuela de ingeniería Eléctrica 
# Modelos Probabilísticos de Señales y Sistemas IE-0405

## Tarea #3
## Elaborada por María Cordero A. (B42016)

### 1. A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.


Como se puede observar, ambas se acercan a curvas gaussianas, por lo que se describirán como tal.
Para obtener las curvas de mejor ajuste, se obtuvo el valor de la media, amplitud y desviación estándar, las cuales son:
- Para x: 
    - Media: 10.0
    - Desviación estándar:3.1691447207203343 $\approx$ 3.17
    - Amplitud: 0.12588326364305466 $\approx$ 0.13
- Para y: 
    - Media: 15.0 
    - Desviación estándar: 6.068450128041075 $\approx$ 6.07
    - Amplitud: 0.06574039037710823 $\approx$ 0.066 
    
Al revisar los valores de las curvas de mejor ajuste, se encuentra que son similares, como se muestra a continuación:
- Para x: 
    - Media: 9.88371412
    - Desviación estándar:3.1691447207203343
    - Amplitud: 0.12178123 
- Para y: 
    - Media: 15.08746267
    - Desviación estándar: 6.77905397
    - Amplitud: 0.06640209
    
Como se puede haber, hubo variaciones entre los resultados, lo cual se puede atribuir a la definición de la función, pero se acercan lo suficiente para confirmar que son distribuciones gaussianas.

### 2. Asumir independencia de X y Y. Analíticamente, ¿cuál es entonces la expresión de la función de densidad conjunta que modela los datos?

Se obtiene entonces para X la siguiente función marginal: <br>
$F_X(x)=\frac{1}{\sqrt{2 \pi 10.04}} e^{\frac{-(x-10)^2}{2 \cdot 10.04}} \approx 0.13\cdot e^{\frac{-(x-10)^2}{20.08}}$

Por otro lado, para Y será de la forma: <br>
$F_Y(y)=\frac{1}{\sqrt{2 \pi 36.83}} e^{\frac{-(x-15)^2}{2 \cdot 36.83}} \approx 0.066 \cdot e^{\frac{-(x-15)^2}{73.66}}$ <br>

Finalmente, la función de densidad conjunta será: <br>
$F_{X,Y}(x,y)=0.13\cdot e^{\frac{-(x-10)^2}{20.08}} \cdot 0.066 \cdot e^{\frac{-(x-15)^2}{73.66}}= 0.00858 e^{\frac{-(x-10)^2}{20.08}+\frac{-(x-15)^2}{73.66}} $

### 3. Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) para los datos y explicar su significado.
Se obtuvo entonces:
- Correlación: Dió un valor de 149.54281 dada la definición para valores discretos, lo cual se considera que es muy alto, por lo que se puede asumir que están altamente correlacionados.
- Covarianza: Se obtuvo un valor de 0.06481, lo cual se dice que está cercano a cero, por lo que se dice que la variación que experimentan ambas variables es independiente una de la otra.
- Coeficiente de correlación: Se observa que fue de 0.00337, es decir, muy cercano a cero, por lo que se dice que ante cambios de una de las variables, la otra no va a reaccionar a éstos (Levine, Krehbiel, Berenson, 2006).

### Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D).
Las funciones se pueden observar en el código .py.

## Bibliografía
- Berenson, M., Levine, D. y Krehbiel, T. (2006). *Estadística para administración*. Pearson Educación.
