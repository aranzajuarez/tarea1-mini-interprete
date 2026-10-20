# Declaración de uso de Inteligencia Artificial

**Actividad:**
**Integrantes:**
**Fecha:**

> Esta declaración es obligatoria en toda tarea, práctica y en el proyecto final.
> **No da ni quita puntos**: es un reporte adicional que se revisa aparte y se
> devuelve con comentarios. **No se evalúa cuánta IA usaron**, sino si pueden
> dar cuenta de lo que entregaron.

---

## 0. ¿Se usó IA en esta actividad?

SI, se utilizó asistencia de inteligencia artificial (Gemini) durante el desarrollo de la Tarea 1 para guiar los pasos del README adecuadamente, verificar la lógica de asociatividad del parser y estructurar la documentación de los casos de prueba dado que aún no dominó el uso de Git.

---

## 1. Herramienta(s) utilizada(s)

| Herramienta | Versión o modelo, si lo saben |
|---|---|
| Gemini| |

> Cuenta también el autocompletado del editor (Copilot y similares). Si sólo
> fue eso, basta con decirlo en un renglón y seguir al punto 4.

---

## 2. Objetivo del uso

| Para qué la usamos | En qué parte del entregable |
|---|---|
| Abrir archivos o identificar cosas en la interfaz de VS Code| |
| Instalar paqueterías o programas | |
| Interpretar errores | |

> Sean específicos. *"Para la tarea"* no dice nada.
> *"Para generar las pruebas de `minimo_de_llaves`"* sí.

---

## 3. Prompts principales

Textuales, tal como los escribieron. No los limpien ni los reescriban.

```
(prompt 1)
```

```
(prompt 2)
```

---

## 4. Cómo se incorporó o se descartó lo obtenido

**Éste es el punto que más pesa.**

| Qué produjo la herramienta | ¿Aceptado, modificado o descartado? | Por qué | Dónde quedó (archivo / commit) |
|---|---|---|---|
| Me daba respuestas concisas de donde buscar los archivos o como usar la terminal| Aceptado | Ddao que no se usar bien la termianl le pedía explicaciones de porque hacerlo así | |
| Me daba los commits necesarios o code o me explicaba que debpia instalar| Aceptado |

> **"Lo descartamos" es una respuesta excelente**, si dicen por qué.
> Una declaración donde todo se aceptó sin cambios es una declaración que
> no muestra criterio.

### 4.1 Si la usaron para el análisis: el contraste

Se les pidió intentarlo primero por su cuenta. Si lo hicieron así:

| | |
|---|---|
| ¿Qué encontró la herramienta que ustedes **no** habían notado? | |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? | **Duplicación de código estructural en el Parser:** La IA inicialmente sugirió reemplazar el `if` por `while` dentro de cada método sin señalar que los métodos `_expresion` y `_termino` son casi idénticos y comparten la misma plantilla de iteración (**duplicación de lógica** y **rigidez**).
- **Amplificación del cambio al añadir operadores:** La IA tiende a enfocarse en que "el código funcione y pase las pruebas", sin advertir inicialmente que agregar un nuevo operador requiere modificar múltiples archivos (`lexer`, `parser` y `evaluator`).|

> La segunda es la que más nos interesa. Una herramienta suele no señalar la
> duplicación de código, porque el programa funciona igual. Ustedes ya saben
> por qué eso sí importa.
>
> Si no usaron IA para el análisis, escriban *"no aplica"*.

### 4.2 ¿Cómo verificaron que lo que incorporaron era correcto?

> Una prueba que escribieron, una ejecución, un contraste contra las notas de
> clase o contra el enunciado. *"Lo revisamos"* no es una verificación.

Revise en internet o use mi criterio

---

## 5. Reflexión

### 5.1 ¿Qué limitación concreta observaron **en esta actividad**?

> Concreta. No *"a veces se equivoca"*, sino *"propuso pruebas sólo para
> m = 4 y nunca para órdenes impares, porque no conocía la definición del
> laboratorio"*.

### 5.2 ¿Qué harían distinto la próxima vez?

---

## Firma

> Declaramos que entendemos y podemos explicar todo lo que entregamos,
> independientemente de las herramientas que hayamos utilizado.

| Nombre | Número de cuenta |
|---|---|
| | |
