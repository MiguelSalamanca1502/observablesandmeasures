# Programa simulacion teoria cuantica basica

Programa que puede calcular varias operaciones de la teoría cuántica básica, tales
como la probabilidad de encontrar una partícula confinada en ciertos puntos, calcular
el conmutador de dos observables, Calcular un estado despues de varios operadores unitarios, 
etc.

Ademas de esto se van a modelar los siguientes problemas:
* 4.3.1
* 4.3.2
* 4.4.1
* 4.4.2
  
y se va a discutir acerca de los ejercicios 4.5.2 y 4.5.3

---
## Comenzando 

Para poder dar uso a esta libreria debe clonar la misma, moverla a la carpeta que desee.

Puede hacer esto usado [Git cmd](https://git-scm.com/downloads), escribiendo lo siguiente:

```
$ git clone https://github.com/MiguelSalamanca1502/observablesandmeasures
```

### Pre-requisitos 

Para correr esta libreria se debe tener instalado:
* Python 3
  
Puede descargarlo desde la pagina oficial de [Python](https://www.python.org/downloads/)

* Libreria NumPy
  
puede descargala desde la pagina oficial de [Numpy](https://numpy.org/install/)

* Libreria MatPlotLib

puede descargarla desde la pagina oficial de [MatPlotLib](https://matplotlib.org/downloads.html)

* Libreria SciPy

puede descargarla desde la pagina oficial de [SciPy](https://www.scipy.org/scipylib/download.html)

---

## Ejecutando las pruebas ️

Para poder ejecutar las pruebas basta con abrir el archivo ObservablesandMeasuresTests.py y ejecutarlo

---

## Construido con

* [Python](https://www.python.org/) - Lenguaje de programacion usado
* [PyCharm](https://www.jetbrains.com/es-es/pycharm/) - El IDE usado
* [NumPy](https://numpy.org/) - Libreria para un mejor manejo de arreglos
* [MatPlotLib](https://matplotlib.org/) - Libreria usada para graficos
* [SciPy](https://www.scipy.org/) - Libreria usada para la constante reducida de Planck
* [Overleaf](https://es.overleaf.com/) - Editor usado para escribir las ecuaciones y tomas capturas de las mismas
* [LaTeX](https://www.latex-project.org/) - Lenguaje de mark up usado para las ecuaciones
---
## Modelado de ejercicios
### 4.3.1
Encuentre todos los posibles estados descritos en el ejercicio 4.2.2 en los que puede transicionar
despues de realizar la medicion.

Para resolver este ejercicio nos vamos a apoyar del postulado que dice que todos los vectores propios
de un obsevable asociado a una cantidad fisica van a ser resultado de la medida de todos los estados
sin importar cual. tambien en el que se nos dice que si el resultado de la medida es un valor propio,
el estado de la medida siempre va a ser el vector propio correspondiente a ese valor propio.

Vamos a tomar el observable del spin en x y vamos a determinar sus vectores propios, estos seran los
estados finales correspondientes a las medidas hechas, con la ayuda de la funcion ex1(), que no recibe
parametros y retorna un vector 2d con los vectores propios (estados finales) despues de la medicion.

Observable de spin para x:

![Observable del spin para x](sx.png)


### 4.3.2
Haga los mismos calculos como en el ejemplo anterior, usando el ejercicio 4.3.1. Luego dibuje la probabilidad
de distribucion de los valores propios como en el ejemplo previo.

Para dar solucion a este ejecicio vamos a hacer los mismos calulos que el ejemplo dado, teniendo el ket
inicial (particula en spin up), y sus estados finales (calculados en el anterior ejercicio), se va a
hacer el producto interno entre estos y hacer el modulo cuadrado para obtener la probabilidad, vamos 
a graficar los valores propios en el eje x y en el eje y las probabilidades pertenecientes a cada vector
propio de su valor propio, usaremos la funcion ex2() que no recibe parametros y retorna None,
solo grafica la distribucion de los valores nombrados.


### 4.4.1
Verifique que las matrices u1 y u2 son matrices unitarias, multipliquelas y verifique que su producto es tambien unitario

Para solucionar este ejercicio, primero vamos a verificar que u1 y u2 son unitarias, multiplicando a cada una por ella
misma y verificar que la matriz resultante sea la matriz indentidad, luego vamos a multiplicarlas entre si y verificar
de nuevo si la matriz es unitaria, usaremos la funcion ex3() que no tiene parametros y retorna None (solo imprime), y isUnitary() que
recibe una matriz y retorna si un valor booleano.

U1:

![u1](u1.png)

U2:

![u2](u2.png)

### 4.4.2
Vaya al ejemplo 3.3.3, mantenga el vector de estado inicial, y cambie el mapa unitario por el dado, determine el estado
del sistema despues de tres pasos de tiempo, ¿cual es la probabilidad de que la bola se encuentre en el punto 3?

Para resolver este ejercio, vamos a multiplicar el mapa unitario por el vector de estado inicial, luego multiplicaremos
de nuevo el mapa unitario pero esta vez por el resultado que obtuvimos, repetiremos este proceso una vez mas y
haremos el modulo cuadrado al valor que esta en la posicion 3, para esto daremos uso a la funcion ex4() que no recibe
parametros y retorna a la funcion prob(), que recibe como parametro el vector de estado, la posicion que se quiere consultar
y retorna la probabilidad de que la bola se encuentre alli.

Mapa unitario:

![unitmap](unitarymap.png)

Vector de estado inicial:

![initstate](initialstate.png)

### 4.5.2
Escriba el estado generico para un sistema de dos particulas con spin, generalizelo para un sistema con n particulas

Cuando el sistema es de dos particulas, los ket de cada particula son los siguientes:

![ket1](uparrow.png)

![ket2](downarrow.png)

y el vector de estado generico para el sistema de ambas particulas es:

![result](tensor2particles.png)

Cuando el sistema es de n particulas, los ket de todas las particulas son los siguientes

![generalvectors](generalvectors.png)

Y luego vamos a calcular el sistema que esta conformado por todas las particulas:

![tensor](generaltensorproduct.png)

### 4.5.3

Asuma el mismo escenario del ejemplo 4.5.2 y sea:

![phi](state453.png)

¿es este estado separable?

Sea

![ket1](state1.png)

![ket2](state2.png)

Y el sistema formado por ambas:

![states](statestensor.png)

Para verificar si alguna particula esta enlazada a otra tendremos que verificar
que:

![ver](verify.png)

Por lo cual planteamos el siguiente sistema de ecuaciones:

![equations](equ.png)

---

## Autores ️

* **Miguel Salamanca** - [MiguelSalamanca1502](https://github.com/MiguelSalamanca1502)