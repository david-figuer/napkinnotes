---
title: "¿Qué tan rápido sale el corcho de una botella de champán?"
author: "Duvier Suarez Fontanella"
date: 2026-03-01
layout: articles
status: published
category: "Dinámica de Fluidos"
tags: ["física", "termodinámica", "champán", "supersónico"]
summary: "Cada descorche de champán es una pequeña demostración de física: gases comprimidos, termodinámica y un corcho convertido en proyectil. Un simple *pop* esconde la fuerza de la presión interna y un chorro de gas que puede acercarse a la velocidad del sonido."
image: images/corcho.png
---

[TOC]



Cuando ves una botella de champán en la mesa, mayestática, elegante, ajena al caos, parece un objeto pacífico.  
No lo es.

Su interior contiene CO₂ disuelto a presiones que oscilan entre **5 y 7 atm**. Es decir, un ambiente ideal para un pequeño festival termodinámico.

Podemos estimar la fuerza que empuja al corcho mediante:

$$
F = P\,A
$$

donde  
- P ≈ 6 × 10<sup>5</sup> Pa  
- A = πr<sup>2</sup>, con r ≈ 9 × 10<sup>-3</sup> m

Entonces:

$$
A \approx 2.54\times10^{-4}\,\text{m}^2
$$

$$
F \approx (6\times10^5)(2.54\times10^{-4}) \approx 150\,\text{N}
$$

Esto equivale al peso de un niño pequeño apoyado sobre un área del tamaño de una moneda.  

Y sí: todo eso está intentando expulsar el corcho hacia tu lámpara del salón.

---

## Desarrollo

Cuando se retira el bozal, el corcho queda sostenido únicamente por fricción.  
El gas, mientras tanto, grita como un aficionado de fútbol encerrado en una cabina de teléfono.

La expansión del gas es tan rápida que puede aproximarse como **adiabática**:

$$
P\,V^\gamma = \text{constante}
$$

con γ ≈ 1.3 para el CO₂.

Durante los primeros milímetros, la presión apenas cae, lo que permite estimar el trabajo inicial como:

$$
W \approx F_0\,\Delta x
$$

Tomemos $\Delta x \approx 0.02\,\text{m}$:

$$
W \approx 150\times0.02 = 3\,\text{J}
$$

La energía disponible se convierte en velocidad para un corcho típico de masa m ≈ 0.007 kg:

$$
v = \sqrt{\frac{2W}{m}}
$$

$$
v \approx \sqrt{ \frac{6}{0.007} } \approx 29\,\text{m/s}
$$

Equivalente a **105 km/h**.  
Si el corcho fuera un atleta olímpico, sería plusmarquista mundial… durante un solo segundo.

El corcho: normalmente no.  
El gas detrás del corcho: absolutamente sí.

Cuando la botella está muy presurizada, el gas sale por el cuello con tal velocidad que alcanza el **flujo ahogado**:

$$
v_{\text{gas}} \approx c_s
$$

La velocidad del sonido en CO₂ es aproximadamente:

$$
c_s \approx 260\,\text{m/s}
$$

Y estudios recientes han medido jets de champán alrededor de v ≈ 300 m/s.

Es decir:  
Aunque el corcho no sea supersónico, la **explosión gaseosa que lo acompaña sí puede serlo**.

A medida que el corcho avanza una distancia x, el volumen disponible aumenta y la presión disminuye según:

$$
P(x) = P_0 \left( \frac{V_0}{V_0 + A x} \right)^{\gamma}
$$

La fuerza es:

$$
F(x) = P(x)\,A
$$

Y la velocidad de salida tras recorrer el cuello de longitud L se calcula como:

$$
v = \sqrt{\frac{2}{m} \int_0^{L} P(x)\,A\,dx }
$$

Para valores típicos:

$$
20\,\text{m/s} \le v \le 40\,\text{m/s}
$$

En condiciones extremas:

$$
v_{\text{ext}} \approx 100\text{–}120\,\text{m/s}
$$

No es un misil intercontinental, pero tampoco algo que quieras recibir en la ceja.

No todos los corchos salen igual. La temperatura importa: más temperatura = más presión; más presión = más energía almacenada. Champán caliente = mala idea.

También influyen la rugosidad y la forma del corcho. Algunos sellan más herméticamente, aumentando la presión antes del despegue. El contenido de CO₂ también cambia el resultado: las botellas jóvenes suelen tener más gas residual. Y la fricción en el cuello determina cuánto cuesta que el corcho empiece a moverse; cuanto mayor sea esa resistencia inicial, mayor será el “latigazo”.

En otras palabras: cada botella tiene su personalidad… y su carácter explosivo.

A 30–40 m/s, un corcho puede causar lesiones serias, desde hematomas hasta daños oculares.  
A más de 100 m/s, estás manejando un proyectil digno de un campo de pruebas de ingeniería.

Consejo universal:

**Nunca apuntes la botella hacia una persona, un animal o un televisor que te haya costado dinero.**

---

## Conclusiones

El despegue del corcho de champán es uno de los ejemplos más entretenidos de física cotidiana.  
Un pequeño objeto de madera comprimida, impulsado por un gas desesperado por expandirse, alcanza velocidades dignas de un vehículo deportivo.

La próxima vez que brindes, recuerda:  
Acabas de asistir al lanzamiento de un *microcohete carbónico* cortesía de la fermentación.

Salud, y buena puntería (pero nunca hacia algo valioso).

---

## Apéndice

Valores típicos de referencia:

- Presión interna: 5–7 atm  
- Masa del corcho: 6–8 g  
- Aceleración inicial: hasta 10<sup>4</sup> m/s² 
- Velocidad típica del corcho: 20–40 m/s  
- Velocidad extrema: 120 m/s  
- Velocidad del gas: 260–300 m/s  

---
