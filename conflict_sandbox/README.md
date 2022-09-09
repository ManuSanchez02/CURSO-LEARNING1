# Conflict Sandbox

Alicia, Berto, Carlos, Victor y Laura tienen nuevos desafíos por resolver,
pero no tuvieron tiempo de coordinar como se van a repartir las actividades.

Decidieron que cada quien intente resolver 6 ejercicios al azar y después van a combinar
las soluciones exitosas.

Cada integrante cargó sus resultados en un branch a su nombre, sin embargo como todos son nuevos
en el uso de git no respetaron las buenas prácticas y mezclaron las soluciones completas con
las que todavía tenían bugs.

Laura arrancó tarde, y viendo la situación decide finalizar el ejercicio que había empezado
y luego dedicarse de compaginar las soluciones de sus compañeros.

Usted nuevamente jugará el rol de Laura.

1) Cree un branch basado en main para su trabajo personal.

2) Elija un ejercicio de cualquier dificultad y resuélvalo. Asegúrese que pasa los testeos de unidad.
*(Mayor kyu implica menor dificultad).*
   
3) Commitee su solución

4) Visite los branches de sus 4 compañeros, alice, Berto, Carlos y Victor, y verifique qué ejercicios resolvió cada uno.
   (`git diff` vs main)

6) Mergee su branch con los de sus 4 compañeros. Al presentarse un conflicto deberá optar
por la solución que pasa todos los testeos de unidad.

7) Al finalizar, su branch deberá pasar el 100% de los testeos de unidad.

**Sugerencias:**
* *Antes de realizar un mergeo, anote los desafíos que completaron sus respectivos testeos de unidad.
Si durante el mergeo ocurre un conflicto en un desafío ya solucionado, quédese con la solución validada.*
* *Antes de commitear un mergeo, corra de nuevo los tests para verificar que no hubieron regresiones.*
* *Puede ayudarse de una ide. Se recomienda el uso de [PyCharm](https://snapcraft.io/pycharm-community)*