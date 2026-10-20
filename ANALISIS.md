# Análisis — Tarea 1

**Integrantes:**
1. Aranza López Juárez

**Fork:**
**Rama:**

> Contesten en este archivo. Respuestas breves y concretas: se califica que
> hayan entendido, no la extensión.

---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?

| Componente | Qué recibe | Qué entrega | De qué es responsable |
|---|---|---|---|
| `lexer` | `str` (texto) | `list[Token]` | Convierte la cadena de texto plano en una secuencia estructurada de tokens, ignorando espacios. |
| `parser` | `list[Token]` | `NodoAST` | Analiza la estructura gramatical dada por los tokens y construye el Árbol de Sintaxis Abstracta (AST) |
| `ast` | N/A (Clases) | Estructura de nodos | Define las clases de los nodos jerárquicos de la expresión en memoria (números y operaciones). |
| `evaluator` | `NodoAST` | `int` o `float` | Recorre recursivamente el AST y calcula el valor numérico final de la expresión. |

### 1.2 ¿Qué recorrido sigue una expresión desde que se recibe como texto hasta que produce un resultado?

> Usen `(3 + 4) * 2` como ejemplo y muestren cómo se ve entre etapa y etapa.

### 1.2 ¿Qué recorrido sigue una expresión desde que se recibe como texto hasta que produce un resultado?

| Etapa | Cómo se ve `(3 + 4) * 2` aquí |
|---|---|
| texto | `"(3 + 4) * 2"` |
| tokens | `[PAR_IZQ, NUMERO(3), MAS, NUMERO(4), PAR_DER, POR, NUMERO(2)]` |
| AST | `Multiplicacion(Suma(3, 4), 2)` |
| resultado | `14` |


> Para el renglón del AST, dibújenlo **primero ustedes** y después comprueben
> con `python3 interprete.py --arbol "(3 + 4) * 2"`. Si su dibujo y el del
> programa no coinciden, uno de los dos está mal, y averiguar cuál es
> justamente el trabajo.

---

## 2. Las pruebas que ya estaban
### 2.1 ¿Qué pruebas venían incluidas?

| Prueba | Componente | Comportamiento que verifica | ¿Cuántos operadores usa? | ¿Normal, frontera o inválida? |
|---|---|---|---|---|
| `test_suma` | `evaluator` | Evalúa el resultado numérico de una suma (`3 + 4` = `7`) | 1 | Normal |
| `test_resta` | `evaluator` | Evalúa el resultado numérico de una resta (`10 - 3` = `7`) | 1 | Normal |
| `test_multiplicacion` | `evaluator` | Evalúa el resultado numérico de una multiplicación (`6 * 7` = `42`) | 1 | Normal |
| `test_division` | `evaluator` | Evalúa el resultado numérico de una división (`10 / 2` = `5`) | 1 | Normal |
| `test_precedencia_sin_parentesis` | `evaluator` | Respeta la jerarquía de operaciones al realizar primero la multiplicación y después la suma (`3 + 4 * 2` = `11`) | 2 | Normal |
| `test_precedencia_con_parentesis` | `evaluator` | Respeta el orden al realizar primer las operaciones dentro del paréntesis y luego las que estén fuera (`(3 + 4) * 2` = `14`) | 2 | Normal |
| `test_tokeniza_un_numero_solo` | `lexer` | Convierte una cadena con solo un número entero en un único token de número | 0 | Normal |
| `test_tokeniza_una_suma` | `lexer` | Convierte la expresión `"3+4"` en tokens de número y suma, dando además sus posiciones | 1 | Normal |
| `test_los_espacios_no_producen_tokens` | `lexer` | Verifica que los espacios en blanco no generen tokens adicionales, obteniendo 3 tokens en la operación ("   3    +    4    ") | 1 | Normal |
| `test_tokeniza_parentesis` | `lexer` | Reconoce correctamente los tokens de paréntesis izquierdo, número y paréntesis derecho | 0 | Normal |
| `test_construye_el_arbol_de_una_suma` | `parser` | Construye el AST correcto para una suma simple (`3 + 4`) | 1 | Normal |
| `test_la_multiplicacion_se_agrupa_antes_que_la_suma` | `parser` | Verifica que `*` se agrupe como subárbol dentro de `+` respetando precedencia | 2 | Normal |
| `test_los_parentesis_cambian_la_agrupacion` | `parser` | Verifica que los paréntesis alteren la agrupación en el AST de la multiplicación, al realizar primero la operación dentro de estos | 2 | Normal |

> Llenen la tabla **completa**, con las 13. Es tediosa a propósito: la única
> forma de saber qué no está cubierto es caracterizar sistemáticamente lo que
> sí. Cuando terminen, léanla como columna, no como renglones, y pregúntense
> qué combinación **no aparece nunca**.

### 2.2 ¿Qué comportamientos **no** estaban probados?

> Ésta es la pregunta importante de toda la tarea. Tómense su tiempo.

1. **Asociatividad de operadores de la misma precedencia**
Notemos que revisamos operaciones de 2 números y 1 operador, pero ¿Qué sucede si tenemos varios operadores del mismo tipo? Según la jerarquía de operaciones, deberán de realizarse de izquierda a derecha, pero falta corroborar que suceda. Además, no probamos cuando se agregan varias veces el mismo operador, ejemplo 10 - 3 - 2 - 1 o 40 / 8 / 5
2. **Números negativos** 
No probamos si en el lexer son admitidas operaciones con valores numéricos negativos, ejemplo  `-34` o `-(2 + 8)`.
3. **Errores de sintaxis específicos en paréntesis:** 
No se incluyeron pruebas que revisen entradas inválidas con paréntesis vacíos `()` o paréntesis que no se cerraron.
4. **Casos frontera con cero en operaciones válidas:** 
No se revisaron casos que presenten al cero, es decir como neutro aditivo o al multiplicarlo (por ejemplo `0 + 5` o `1 * 0`).

---

## 3. Las pruebas que agregaron

Agregamos 7 nuevas pruebas en `tests/test_evaluator.py`.

### 3.1 ¿Cuáles son casos normales, cuáles frontera y cuáles inválidos?

| Prueba (archivo::nombre) | Entrada | Esperado | Categoría | ¿Por qué esa categoría? |
|---|---|---|---|---|
| `tests/test_evaluator.py::test_evalua_multiples_operaciones_combinadas` | `"10 + 5 - 2"` | `13` | Caso Normal | Evalúa la combinación de múltiples operadores de la misma precedencia en una expresión lineal. |
| `tests/test_evaluator.py::test_evalua_expresion_con_subparentesis` | `"(10 + 2) * (8 / 4)"` | `24.0` | Caso Normal | Valida la evaluación correcta de múltiples subexpresiones agrupadas por paréntesis. |
| `tests/test_evaluator.py::test_evalua_restas_encadenadas_asociatividad` | `"10 - 3 - 2"` | `5` | Caso Frontera | Revisa el funcionamiento de la asociatividad en restas continuas sin paréntesis, revela la asociatividad a la derecha del código. |
| `tests/test_evaluator.py::test_evalua_divisiones_encadenadas_asociatividad` | `"12 / 4 / 2"` | `1.5` | Caso Frontera | Revisa la asociatividad a la izquierda en divisiones sucesivas, evaluando la presición aritmetica. |
| `tests/test_evaluator.py::test_evalua_division_entre_cero` | `"10 / 0"` | Lanza `ErrorDeEvaluacion` | Caso Frontera | Controla la excepción en el límite aritmético de división por cero evitando que falle el sistema con un error no controlado. |
| `tests/test_evaluator.py::test_rechaza_menos_unario` | `"-3"` | Lanza `ErrorDeSintaxis` | Entrada Inválida | Valida el rechazo sintáctico de números negativos directos no permitidos por la gramática declarada. |
| `tests/test_evaluator.py::test_rechaza_parentesis_vacios` | `"()"` | Lanza `ErrorDeSintaxis` | Entrada Inválida | Comprueba la detección inmediata de agrupaciones vacías sin expresiones válidas en su interior. |

---

## 4. Los defectos

### 4.1 ¿Qué defecto reveló primero una prueba nueva?
Reveló que había un error en el código, dado que no se respetaba la asociatividad a la izquierda en operadores con la misma precedencia sin paréntesis, usamos ejemplos de resta y división.

### 4.2 ¿Por qué el comportamiento observado era incorrecto?

> No basta con "daba mal". Digan contra qué lo están comparando: qué regla,
> qué línea de la semántica declarada del README.

En la especificación del README y la semántica estándar de expresiones aritméticas, es decir la Jerarquía se Operaciones, los operadores del mismo nivel se deben asociar de izquierda a derecha, así en nuestro ejemplo al evaluar la entrada `"10 - 3 - 2"`, el programa arrojaba el valor de `9`, dado que agrupaba las operaciones de derecha a izquierda, realizando `10 - (3 - 2) = 10 - 1 = 9`. Según la semántica vista, debería de haberse agrupado como `(10 - 3) - 2 = 5`.

### 4.3 ¿Qué cambio realizaron?

| Defecto | Entrada que lo revela | Daba | Debería dar | Commit rojo | Commit verde |
|---|---|---|---|---|---|
| Asociatividad a la derecha en resta | `"10 - 3 - 2"` | `9` | `5` | `236becc` | `052250b` |
| Asociatividad a la derecha en división | `"12 / 4 / 2"` | `6.0` | `1.5` | `236becc` | `052250b` |

### 4.4 ¿Cómo saben que la corrección es general y no sólo hace pasar ese ejemplo?
Porque se cambió el mecanismo de construcción del AST en la gramática del `Parser`. Al sustituir la llamada recursiva por un bucle iterativo `while` (`nodo = OperacionBinaria(op, nodo, derecho)`), la estructura de acumulación nos garanizará que los operadores de la misma precedencia en una secuencia se acumularán en un subárbol a la izquierda, sin importar el tamaño de la cadena presentada. 

---

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontraron?

> Al menos dos. Usen el vocabulario de clase: duplicación, rigidez,
> acoplamiento alto, condicionales repetidos, amplificación del cambio.

1. **Duplicación de lógica de parseo en `Parser`:** Los métodos `_expresion` y `_termino` comparten exactamente la misma estructura de control e iteración, diferenciándose únicamente en el conjunto de tokens de operadores (`OPERADORES_SUMA` vs `OPERADORES_PRODUCTO`) y en el siguiente nivel de precedencia que invocan (`_termino` vs `_factor`).
2. **Condicionales repetidos / Rigidez para añadir operadores:** Para agregar un nuevo operador (como `%` o `**`), hay que modificar manualmente las tuplas de tipos de tokens y alterar o añadir nuevos métodos en el `Parser`, aumentando la probabilidad de errores por modificación en múltiples lugares (**amplificación del cambio**).

### 5.2 ¿Qué refactorización realizaron, y por qué conserva el comportamiento?

> "Las pruebas siguen pasando" es parte de la respuesta, pero no toda.
> ¿Por qué el cambio es equivalente?

Se refactorizaron los métodos de `_expresion` y `_termino` para usar bucles iterativos `while`. Se conserva el comportamiento porque es un cambio estructural equivalente en las expresiones de 2 términos (caso base), pero se corrige la precedencia al asociar hacia la izquierda en expresiones de 3 o más términos. Las 20 pruebas automáticas en `pytest` certifican que no hubo regresiones.

### 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?

> Justifiquen. **"Ninguno" puede ser la respuesta correcta.** Si dicen que sí,
> digan qué problema concreto resuelve y qué costo tiene. Si dicen que no,
> digan qué tendría que cambiar en el sistema para que empezara a convenir.

**Ninguno.**
- **Factory Method:** No es necesario porque la creación de nodos de AST (`Numero`, `OperacionBinaria`) es directa.
- **Adapter:** No hay interfaces incompatibles de terceros ni librerías externas que requerimos adaptar al sistema.
- **Costo de agregarlos:** Introducir cualquiera de estos patrones añadiría clases abstractas e indirecciones innecesarias para la escala actual de la tarea.

### 5.4 ¿Qué parte del sistema sería más difícil de modificar si se agregara un operador nuevo?
La parte más compleja de modificar sería el **`Parser`**, seguido del **`Lexer`** y el **`Evaluator`**:
1. En el **`Lexer`**: Añadir el nuevo `TipoToken` y su regla en la tokenización.
2. En el **`Parser`**: Asignar el operador al nivel de precedencia adecuado o crear un nuevo método si tiene una precedencia distinta (por ejemplo, potencia `**`), modificando las tuplas de operadores.
3. En el **`Evaluator`**: Añadir la rama correspondiente en la evaluación del AST.

---

## Antes de la declaración: inténtenlo primero ustedes

Usar IA o no es decisión de cada quien, y el curso la permite. Pero **les
pedimos, por favor, que primero hagan el análisis por su cuenta.**

No es una prueba de honestidad. Es que el orden cambia lo que aprenden:

1. **Primero ustedes.** Lean el código, corran las pruebas, escriban sus
   respuestas. Aunque queden incompletas, aunque no encuentren todo.

2. **Después, si quieren, la IA** — pero como contraste, no como sustituto.
   Y entonces contesten dos preguntas, en `DECLARACION_IA.md`:

   - **¿Qué encontró que ustedes no habían notado?**
     Eso es aprendizaje, y se declara sin ninguna pena.

   - **¿Qué *no* encontró, que en este curso sí consideramos un problema?**
     Ésta es la interesante. Una herramienta suele decir que el código
     "funciona bien" y no señalar, por ejemplo, la **duplicación** — porque
     duplicar no rompe nada, el programa corre igual. Pero ustedes ya saben
     por qué eso sí es un mal diseño, y saben nombrarlo. La herramienta no
     tomó esa clase.

> Si invierten el orden se pierden justamente lo segundo: **no se puede notar
> lo que a una herramienta le faltó si uno nunca se formó una opinión propia
> antes de preguntarle.** Y que un programa funcione no implica que esté bien
> diseñado — eso lo dijimos en clase mucho antes de esta tarea.

---

## Declaración de uso de Inteligencia Artificial

Va en `DECLARACION_IA.md`, no aquí. Es obligatoria, pero **no da ni quita
puntos**: es un reporte adicional que se revisa aparte y se les devuelve con
comentarios.

**No se evalúa cuánta IA usaron.** Se evalúa si pueden dar cuenta de lo que
entregaron. *"No usamos"* es una declaración válida y completa; *"lo
descartamos porque..."* es de las mejores respuestas posibles.
