# Listas ()

*Agregar elementos a una lista: _append_

~~~python
miLista.append("nuevo_elemento")
~~~

*Agrenar elemento en una posición determinada: _insert_

~~~py
miLista.insert(2,"nuevo_elemento")
~~~

*Agregar varios elementos al final: _extend_

~~~py
miLista.extend("elemento1","elemento2","elemento3")
~~~

*Localizar la posición de un elemento: _index_

~~~py
print(miLIsta.index("elemento"))
~~~

* Comprobar si un elemento se encuentra en la lista. Esto devolverá un true si se encuentra o un fasle si caso contario

~~~py
print("elemento" in miLista)
~~~

* Eliminar un elemento: _remove_

~~~py
miLista.remove("elemento")
~~~

* Eliminar el último elemento: _pop_

~~~py
miLista.pop()
~~~

* Añadir una lista a otra

~~~py
miListaFinal = miLista1 + miLista2
~~~

## Tuplas [ ] son listas que no se pueden modificar

* Podemos convertir una tupla en lista con _list_

~~~py
milista=list(mitupla)
~~~

* Y para convertir una lista en tupla con _tuple_

~~~py
mitupla=tuple(milista)
~~~

* Para averiguar si un elemento se encuentra en una tupla (vale también para las listas) podemos usar dos opciones. La primera nos devolvera verdadero o falso. La segunda el número de veces que aparece

~~~py
print("elemento" in mitupla)
~~~

~~~py
print(mitupla.count("elemento"))
~~~

* Para averiguar la longitud de una tupla

~~~py
print(len(mitupla))
~~~

* Empaquetado de tuplas, para asignar los distintos valores de una tupla a diversas variables

~~~py
mitupla=("Diego", 1, 5, 1969)
nombre, dia, mes, year = mitupla
~~~

## Diccionarios { } como los arrays asociativos de PHP. Estruccturas clave:valor

---

## Varios

* Aumentar un contador

~~~py
variable+=1
~~~
