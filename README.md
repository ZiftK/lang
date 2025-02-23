#Lenguaje .lang
## ¿Qué es lang?
Es un lenguaje interpretado que permite realizar operaciones con los objetos matemáticos:
  - palabra
  - lenguaje
  - alfabeto

## ¿Cómo usarlo?
El interprete de lang está hecho con python, por lo que para correr lang en tu dispositivo necesitas
tener python 3.11 o superior instalado.

### Pasos para instalarlo
  1. Descarga el **.zip** del repositorio o **clonalo**
  2.  Ejecuta **pip install .** en la carpeta **LangOp** dentro del entorno virtual donde desees instalar **lang**

### Ejecutar ficheros .lang
Para ejecutar cualquier archivo **.lang** sólo es necesario ejecutar el comando `lang <ruta de archivo .lang>`,
el interprete está en una versión muy temprana, así que disculpa la poca información que brinda respecto a los errores.

# Tipos

## String
### Definiciones y reasignaciones
Son palabras y se pueden definir usando la siguiente sintaxis
```
String word1 = "ab cd ef";
```
Todo lo que esté entre `""` será considerado parte de la palabra.
Se puede cambiar en cualquier momento el contenido de la variable `word1` reasignando su valor,
además podemos visualizar el contenido de la variable usando la sentencia `show`.

```
String word1 = "ab cd ef";
word1 = "2222";
show word1;
```
### Operaciones
  1. `*` -> Operador de concatenación; concatena dos palabras `palabra1*palabra2`
  2. `^` -> Operador de elevación; eleva una palabra al expontente entero establecido `palabra1^2`
  3. `||` -> Operador de longitud; calcula la longitud de una palabra `| palabra1 |`
  4. `|on|` -> Operador de longitud sobre alfabeto; calcula la longitud de una palabra sobre un alfabeto dado `|palabra1 on alfabeto1|`
  5. `suffixof` -> Operador de sufijos; calcula todos los sufijos de la palabra y los vuelve un lenguaje `suffixof palabra1`
  6. `prefixof` -> Operador de prefijos; calcula todos los prefijos de una palabra y los vuelve un lenguaje `prefixof palabra1`
  7. `subsequenceof` -> Operador de subsecuencias; calcula todas las subsecuencias de una palabra y las vuelve un lenguaje `subsequenceof palabra1`
  8. `substringof` -> Operador de sub cadenas; calcula todas las sub cadenas de una palabra y las vuelve un lenguaje `substringof palabra1`


## Int
### Definiciones y reasignaciones
Son valores enteros y pueden definirse usando la misma sintaxis que se usa para definir palabras.
```
Int a = 1, b = 2;
a = 3;
b = 4;
```
### Operaciones
  1. `+` -> Operador de suma
  2. `-` -> Operador de resta
  3. `/` -> Operador de división entera
  4. `*` -> Operación de multiplicación
  5. `^` -> Operación de elevación

## Alfabetos
### Definiciones y reasignaciones
Son el conjunto de unidad mínima para un lenguaje y se definen con la siguiente estructura.
```
Alph alp1 = {"a", "b", "c"}, alp2 = {"ef", "gh"};
```
### Operaciones
  1. `+` -> Operador de unión
  2. `*` -> Operador de concatenación
  3. `**` -> Operador de clausura de Kleene; se usa a pasos para lidiar con los infinitos; `alp1**10` calcula los 10 primeros elementos de la clausura de Kleene
  4. `*+` -> Operador de clausura positiva; se usa a pasos para lidiar con los infinitos; `alp2**10` calcula los 10 primeros elementos de la clausura positiva

## Lenguajes
### Definiciones y reasignaciones
Son el conjunto de unidad mínima para un lenguaje y se definen con la siguiente estructura.
```
Lang lan1 = {"a", "b", "c"}, lan2 = {"ef", "gh"};
```
### Operaciones
  1. `+` -> Operador de unión
  2. `*` -> Operador de concatenación
  3. `**` -> Operador de clausura de Kleene; se usa a pasos para lidiar con los infinitos; `alp1**10` calcula los 10 primeros elementos de la clausura de Kleene
  4. `*+` -> Operador de clausura positiva; se usa a pasos para lidiar con los infinitos; `alp2**10` calcula los 10 primeros elementos de la clausura positiva


