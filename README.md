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
## Definiciones y reasignaciones
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
  3. `suffixof` -> Operador de sufijos; calcula todos los sufijos de la palabra y los vuelve un lenguaje `suffixof palabra1`
  4. `prefixof` -> Operador de prefijos; calcula todos los prefijos de una palabra y los vuelve un lenguaje `prefixof palabra1`
  5. `subsequenceof` -> Operador de subsecuencias; calcula todas las subsecuencias de una palabra y las vuelve un lenguaje `subsequenceof palabra1`
  6. `substringof` -> Operador de sub cadenas; calcula todas las sub cadenas de una palabra y las vuelve un lenguaje `substringof palabra1`


## Int

