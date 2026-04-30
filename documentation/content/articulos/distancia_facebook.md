---
title: ¿Cuál es la distancia promedio entre dos personas en Facebook?
author: Duvier Suarez Fontanella
date: 2026-04-15
layout: articles
status: published
category: Ciencia de Datos
tags:
  - redes sociales
  - teoría de grafos
  - small world
  - seis grados de separación
summary: El mundo (online) es más pequeño de lo que pensamos, estamos muy cerca unos de otros.
image: images/face_dist.png
---

[TOC]

## Resumen

La hipótesis de que todos estamos conectados por unas pocas relaciones intermedias dejó de ser una anécdota sociológica para convertirse en un resultado matemático cuantificable. Este artículo analiza **la distancia promedio entre dos usuarios de Facebook**, revisa el concepto de **seis grados de separación** y explica, desde la teoría de grafos y los modelos de **mundos pequeños**, por qué estas cifras son tan sorprendentemente bajas en redes de escala global.

---

## Introducción

Meta ha publicado en diversas ocasiones análisis sobre la longitud promedio de los caminos en su grafo social. Los resultados convergen sistemáticamente en un rango entre **4 y 4.7 saltos**.

En su estudio más citado (Facebook Research, 2016), utilizando miles de millones de nodos y decenas de miles de millones de aristas, se obtuvo:

- **Distancia promedio global:** 4.57  
- **Distancia promedio entre usuarios activos en EE. UU.:** alrededor de 4.2  
- **Máxima componente conexa:** > 99 % de la red

Es decir, **cualquier persona en Facebook puede llegar a otra mediante poco más de cuatro intermediarios**. Dicho de otro modo: los “seis grados” ya no son seis.

La idea de los seis grados de separación nació en 1929 con Frigyes Karinthy, se popularizó en 1967 con el experimento de Stanley Milgram y terminó convertida en un concepto cultural. Pero matemáticamente, el fenómeno posee base sólida.

Milgram encontró longitudes promedio cercanas a **5.5 pasos** para conectar a un ciudadano cualquiera con un objetivo elegido. Aunque el diseño experimental tenía sesgos, reveló la estructura de mundo pequeño en redes humanas.

Con datos completos de grafos sociales actuales, hoy se puede afirmar:

- La distancia promedio **no solo es menor que seis**, sino que **se estabiliza por debajo de cinco** en redes con miles de millones de nodos.  
- Este fenómeno no implica que todos se conozcan; solo que **la estructura combinatoria del grafo permite trayectorias muy cortas**.

---

## Desarrollo

Podemos representar Facebook como un grafo no dirigido G = (V, E), donde:

- V es el conjunto de usuarios  
- E es el conjunto de relaciones de amistad  

La **distancia** entre dos vértices u y v, denotada d(u,v), es la longitud mínima del camino que los conecta.

El objetivo es calcular el **average path length** (APL):

$$
L = \frac{1}{|V|(|V|-1)} \sum_{u \neq v} d(u,v)
$$

En redes a gran escala esta suma explícita es inviable. Facebook utiliza técnicas como **BFS aproximado**, **muestreo aleatorio de vértices** y algoritmos distribuidos tipo **HyperANF** para estimar la distribución de distancias.

El comportamiento observado en Facebook coincide con el modelo de **redes de mundo pequeño** (Watts & Strogatz, 1998), caracterizado por:

1. **Alta agrupación (clustering coefficient C)**  
2. **Caminos cortos con crecimiento logarítmico: L ≈ log N**
   
Si N ≈ 10<sup>9</sup>, entonces:

$$
\log(N) \approx 21
$$

Esto sugiere que incluso una red inmensa puede tener caminos sorprendentemente cortos si se cumplen dos condiciones:

- Existe fuerte conectividad local (comunidades).  
- Hay enlaces aleatorios que actúan como “atalayos” en el grafo.

Facebook cumple ambos requisitos: abundan las comunidades de amigos, pero también los contactos distantes geográfica o socialmente. Esos enlaces reducen drásticamente L.

En teoría de grafos, esta propiedad se explica por:

- **Distribuciones de grado con colas pesadas (scale-free)**.  
- **Hubs con grado extremadamente alto**.  
- **Coeficiente de agrupación elevado**, mayor que el de redes aleatorias tipo Erdős–Rényi.

Todo esto importa porque entender distancias promedio permite modelar **difusión de información**, **propagación de epidemias**, **viralidad** y **resiliencia estructural**. Un APL bajo implica expansiones rápidas y pocas etapas de transmisión.

También tiene implicaciones sociales y éticas: las redes acortan el mundo, pero también **amplifican externalidades** como rumores, polarización y contagios culturales. La estructura de mundo pequeño regula la conectividad, pero no la calidad de los vínculos.

Y, desde el punto de vista de ingeniería de plataformas, estas métricas ayudan a mejorar algoritmos de recomendación, especialmente los basados en friends-of-friends, optimizar buscadores sociales, diseñar mecanismos de privacidad basada en distancias y construir sistemas distribuidos que explotan el comportamiento logarítmico de L.

---

## Conclusiones

Las distancias sociales que intuíamos desde hace un siglo son hoy métricas verificables en redes de escala planetaria. Facebook muestra que:

- La distancia promedio entre dos personas es **menor de cinco pasos**.  
- La teoría de **mundos pequeños** predice y explica este fenómeno.  
- Los **seis grados de separación** no solo se mantienen: se comprimen.

La combinación de teoría matemática, datos masivos y modelización computacional revela que vivimos en un mundo sorprendentemente bien conectado.
