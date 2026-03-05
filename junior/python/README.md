# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## 🚀 Cómo Empezar

### Opción 1: Solución en TypeScript
```bash
cd typescript
npm install
npm start
```

### Opción 2: Solución en Python
```bash
cd python
python3 main.py
```

## ✅ Casos de Prueba

Tu solución debe pasar los siguientes casos de prueba:
- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 📝 Tu Solución

Deja acá el link a tu video explicando tu solución con tus palabras

Link: https://youtu.be/x2ZbIWKekYw 
---

## 💰 Bonus (Opcional)

Si completaste alguno de los ejercicios bonus, explica tu solución aquí:

### Bonus Implementado
#### Opción 2 rectángulos superpuestos:




### Explicación del Bonus
*[Explica cómo adaptaste tu algoritmo para resolver el bonus]*
Para resolver el bonus considere el area total como el area de ambos rectángulos menos el "overlap" o la área superpuesta y luego dividi en ambos lenguajes para obtener el número entero más grande para representar el total de paneles solares
Originalmente pense en plantear algunos casos borde que complicaban el algoritmo como cuanto crece el ancho o alto del techo al juntar ambos rectángulos ya que esto podría causar que un panel que antes no entraba ahora pudiera entrar pero para eso necesitaba también saber el desde donde sucede la intersección porque así varía cuanto crece el ancho o el largo

#### Problema con el bonus: Para el caso de testeo 2:
```json
{
      "panelW": 1,
      "panelH": 2,
      "roofW": 3,
      "roofH": 5,
	  "overlap":{
		"width":2,
		"height":2
	  },
      "expected": 12
    }
```
 Obtuve un total de 13 paneles pero en la práctica sólo caben 12 dado que a no ser de que no encontrara el orden óptimo, cualquier orden que probe en papel me dejaba 2 cuadrados 1x1 como resto y mi código no tomaba en cuenta la posición de estos, sumando el último panel.

Para lograr abordar este caso correctamente la única solución que se me ocurrió era simular la forma de los rectángulos con matrices y tener en cuenta la posición en la que se iban insertando los paneles pero debido a la complejidad finalmente decidí dejar el código como esta por lo que El test 2 del bonus retorna fallido durante su ejecución.

---

## 🤔 Supuestos y Decisiones


*Razon de las múltiples funciones y cambios fuera de la función original*:

	- Si bien las instrucciones indicaban que la solución debía ser una sola función que recibiera las dimensiones quise implementar funciones auxiliares para terminar con un código más limpio y fácil de entender.

	- También quise que las funciones tuvieran responsabilidades claras y que fueran fácilmente reutilizables, pudiendo haber incluido el mismo código directamente en la función original, espero que esto no sea un problema ya que lo hice asi principalmente por una maña mía y porque quise que quedara más ordenado o "a mi pinta".

	- Cree un test_cases_overlap.json para testear la solución al problema opcional e incluí algunos casos borde que pense el el json original para mis pruebas

*Supuestos del código*:

	- Cree la función auxiliar check_panel_dimensions que recibe las dimensiones del techo y panel para pasar por un filtro que entrega un booleano que representa si el panel cabe en el techo ya sea horizontal o verticalmente
	
	- Si el panel cabe de alguna forma en el techo se obtiene la cantidad de paneles dividiendo con "//" en python para obtener el entero de la división y Math.floor() para obtener lo mismo de la división en Typescript
    
	- Cree la clase overlap_dict porque prefiero acceder a los valores usando objeto.valor en lugar de objeto["valor"]
    
	- Decidi usar un diccionario para el overlap porque en algunos casos sus dimensiones pueden afectar el resultado
		EJ: Si tienes un panel 1x5 y 2 rectangulos 4x2 con un overlap 1x1 puedes quedar con un width total de 5 cambiando el resultado

Gracias por leer mi README y tomar en cuenta mi postulación!

Tomás Gaete B.