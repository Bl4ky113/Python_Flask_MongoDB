# Curso Básico de Mondongo DB

Gooddamit, no tengo las skills de Backend con APIs para este curso, lo mejor es 
volver cuando las sepa. hoy 06/06/22. Escribire cuando vuelva.

Hello. Dios, ha sido tanto tanto tiempo, me da melancolía volver por acá.
Han pasado exactamente 3 meses desde que deje este mensaje. Hoy 08/06/2022 vuelvo 
a retomar mi ruta de aprendizaje.

Bueno, depues de examenes y demás cosas. Puedo volver. Ya voy para cuatro meses.

start: 09/06/2022
end: 

sessions:
1. 09/06/2022: ... - 20:18
2. 09/07/2022: ... - ...
3. 09/08/2022: 10:15 - ...
4. 09/27/2022: 13:50 - ...
5. 10/06/2022: 15:40 - 19:..
6. 28/10/2022: 13:47 - 

## Que vamos a ver?

- Que son las db noSQL
- Uso de MongoDB con cli, MongoDB compass o un lenguaje de programación
- Pasar Cluster de nuestra db a producción.

Proyecto vamos a hacer una API rest para nuestra DB.

## DBs No SQL

Las DBs NoSQl generalmente se basan en:
- Key - Value:
	Tipo Obj o hash values
- Graphs
	Basado en la teoria de graphs, o multiple relaciones relaciones de un obj
- Wide Column
	Parecida a la estructura de una tabla de filas y columnas, que tiene gran rápidez y capacidad. 
- Documents
	Los datos se pueden guardar en archivos en formato JSON. Y estos se pueden guardar en colecciones.

## Definición de MongoDB 

Es una DB No Relacional, basada en Documents. Creada, Desarrollada y mantenida por la Empresa Mongo.
Es Open Source y Gratuito.

Los Documentos se basan en BSON, o JSON en Binario. 

La DB es divida, separandose para convenencia, esto se le conoce como Cluster de la DB, de MongoDB.
Esta convenencia nos permite escalar la DB de una forma más sencilla, simplemente agregando otro 
servidor para hacer el proceso y manejo de la DB.

No tiene Squema, nos permite almacenar los documentos con diferentes estructuras.

Queries, índices y agregaciones. Con el que basicamente es JS.

## Ecosistema de MongoDB

MongoDB nos permite usar un MongoDB server. El cual vamos a usar.
De este se puede usar la versión comunity, Open Source. Atlas que es 
la basada en Cloud y Enterprise, que es con licencia de Mongo y demás empresas.

Con MongoDB Shell vamos a poder usar nuestro MongoDB Server, aunque podemos usar 
MongoDB Compass que es una GUI. Para hacer Queries, Índices y Agregaciones.

Usaremos conectores para comunicar un lenguaje de programación con el MongoDB Shell y 
MongoDB Server.

Se puede hacer un MongoDB Mobile, que es una instancia local para hacer queries y demás.
Y se puede usar Stitch para agregar funciones lógicas a la DB para hacerla Serverless.
Se puede usar MongoDB Charts para hacer business inteligence.

## Hello MongoDB Atlas

Vamos a usar MongoDB Atlas de Mongo para hacer practicas de MongoDB en Cloud.
Esto nos va a permitir usar el MongoDB Server sin tener que mantener los 
servidores de la DB cómo tal. Tiene algunos beneficios cómo:
- Alta disponibilidad y Seguridad
- Escabilidad
- Disponible en AWS, GCP y Azure
- Fácil monitoreo y optimización

Simplemente vamos a ir a la pag web, registrarnos. Y desde el inicio 
Mongo nos invita a crear un Cluster al momento de registrarnos, pero 
podemos hacer uno desde la pestaña de DBs deployments. Donde podemos ver 
todos nuestros clusters.

Pero antes de usar los Clusters vamos a tener que crear un sistema de seguridad para 
acceeder a nuestra DB, se puede usando keys, como en SSH o usando usuarios con 
contraseñas. Ademas de tener una white list de IPs que pueden acceder a nuestra DB.

## Instalar MongoDB en Linux

Se descarga desde un repo de linux o directamente desde su sito web y agregandolo al path.

Hay problemas de creo permisos o archivos corrompidos, entonces me va a tocar borrar todo 
relacionado a mongodb y volver a instalarlo.

Al parecer he terminado de instalar MongoDB, pero me ha tocado usar en otro computador, ya 
que mongoDB no funciona en Procesadores más viejos que las series de 2012. Tanto Intel como AMD.
Pero lo bueno es que ver mi setup de trabajo en una pantalla 4k, es espectacular y sinceramente 
maravilloso.

He obtenido mi propio PC Poratíl, un i3 de 11va gen, 3.coso Ghz de pura potencia, 
debe correr sin problemas.

## Conectarse a nuestra DB en Atlas desde MongoSH

Vamos a ir al sitio web de Atlas, vamos a ir al menu de DB, y le damos a connect a la DB deseada.
Nos daran varias opciones, elegimos MongoShell, la cual nos va a dar un comando para copiar y pegar.
Podemos jugar con el URL del comando para cambiar o seleccionar una db. Lo ejecutamos, ingresamos 
nuestro usuario de db y podemos usar MongoShell.

## Conectarse a nuestra DB en Atlas desde Compass

Vamos a ir al ..., selecionamos connect desde Compass. Nos dara una Str de connection, lo copiamos en make new connection en Compass. 
Miramos la configuración, generalmente poner la contraseña y eso. Y ya estamos conectados.

## Drivers de MongoDB

Los Drivers de MongoDB es una forma de conectarnos con el cluster de MongoDB, principalmente haciendo procesos mucho más 
automatizados con código. En general son Librerias con las cual vamos a conectarnos, aunque hay alguna que otra que tiene 
cosas extras.

Generalmente vamos a crear una instancia de MongoClient para conectarnos a la DB y crear una Intancia de MongoDatabase,
para despues Obtener los datos de las collections con MongoCollections, en la cual vamos a hacer 
operaciones CRUD en nuestra DB.

## Estructura MongoDB

MongoDB tiene una estructura jerarquica, empezando por DB, Collection, Document y SubCollections.

- DB:
	Contiene Collections. En un cluster puede tener varios de estos.
- Collection:
	Agrupación de Docs. Equivalente a las Tablas, pero sin esquemas de datos.
- Documents:
	Registro de los datos, guardado en BSON, aunque sea analogamente un JSON. Que escencialmente 
	es una mejora de JSON, con más datos y guardado en Archivos binarios

## Operaciones CRUD en MongoShell

- show []:
	Muestra los datos disponibles

	- dbs databases: DBs disponibles, y tamaño
	- collections, tables: Collections en las DBs

- use [db]:
	Usa la DB enviada

- db: Objeto propio de la DB conectada

- db.collection: Obj de la collection llamada

- db.collection.insertOne({JSON OBJ}):
	Inserta el OBJ JSON a nuestra collection, si la collection no existe, la crea.
	Al insertarlo, nos va a hacer return de proceso hecho y el ID del Documento.

- db.collection.insertMany({}, {}, {}):
	Inserta varios JSONS.

- db.collection.findOne({FILTRO EN JSON}):
	Busca el primer doc de la collection que cumpla con un filtro dado en JSON

- db.collection.find({FILTRO EN JSON}):
	Busca los Docs de la collection con un filtro JSON, que generalmente es un mini JSON con la propiedad que se busca
	
	Podemos agregar diferentes modificadores para las busquedas de find, como:
	- pretty: hacer el JSON más legible en la terminal
	- count: contar cuantos resultados son en total

- db.collection.updateOne({FILTRO}, {$set: {CAMBIO}}):
	Actualiza un Doc con {FILTRO}, los datos de {CAMBIO}	
	Retorna true si logra hacer el cambio y cuantos docs cambio

- db.collection.updateMany():
	Lo mismo que el otro, pero a varios docs

- db.collection.deleteOne/Mane({Filtro}):
	Elimina los Docs del filtro, retorna si lo hizo bien y cuantos borro.

Para hacer estas Operaciones en Compass, es bastance sencillo, solo toca seguir la GUI.

## Tipos de Datos en MongoDB

- Strings: Texto, "texto"
- Bools: Booleano, T / F
- ObjectId: El Id o index de un obj o doc, ObjectId("id")
- Date: Formato de Fecha especial de MongoDB, ISODate("fecha")
- Number: Varian en tamaño:
	- Double: decimales
	- Int 32bits
	- Int 64bits
	- Decimal: Numeros grandes de 128bits
- Embedded Docs: Subdocumentos dentro de los documentos, tambien conocidas como subcollections
- Arrays: Una lista que permite los datos anteriores.

Los Documentos de MongoDB tienen un Limite de 16 MB, o Mega Bytes.

## Esquemas y Relaciones

Los esquemas es la forma en la que podemos guardar nuestros Docs, comportandose como un 
espectro. Donde se tiene MongoDB y las DB SQL cómo extremos. 
En MongoDB, se puede guardar todo tipo de Doc, inclusive sin tener la minima estructura parecida 
u tipos de datos, se puede hacer pero no es recomendable ya que necesitariamos hacer queries muy 
complejos para obtener los datos.
En el medio, podemos tener docs con estructuras similares, solo que falten o se agregen algunos campos
en algun que otro documento, pero que en general todos tengan unos datos base.
En DBSQL todos los documentos tienen los mismos tipos de datos y datos, si algun documento necesitara 
un valor vacio, se usa null o valores predeterminados. Haciendo que si un doc tenga que agregarse un
nuevo valor, tendriamos que hacer un script de balanceo para que todos los documentos tengan ese 
tipo de dato, aun así sea un null.

Las Relaciones son la forma en que las collections y los documentos que tienen se relacionan, 
generalmente son de grupos más grandes a pequeños. Como de Carrera > Curso > Clase > Material.
Estas se pueden hacer como en el mundo SQl, creando collections con docs de valores y agregarles 
el ID de otro Documento, al que pertenecen.

## Relaciones Entre Documents

Las relaciones entre Documentos son casos en los que vamos a 
tener que linkear información extra de uno al otro. Lo más general es 
usar Documentos embedidos, cuando la relacion sea 1 : 1, o cuando solo 
ese documento necesite del otro. Como un comentario en un post.

Si más de un documento necesita de ese documento extra, como una etiqueta,
podemos repetir la información de ese documento para cada documento, aunque pueda 
ser no optimo. Ya si esta información debe cambiar en cada documento frecuentemente,
lo mejor sería hacer un documento extra y no un embedded doc, y hacer referencia al ID 
de este.

## Operadores y Filtros en MongoDB

Primero veamos los filtros, los filtros tienen el formato
{ \<field\>: { \<operator\>: \<value\>}, {}, ... }

Con los Queries podemos obtener los docs poniendo filtros, pero 
ademas podemos obtener solo partes de estas usando proyecciones:
{FILTRO}, {value1: 1, value2: 1}
Siguendo este formato, nos traera solo value 1 y 2 de los docs que entren en el FILTRO

### Operadores de Comparación
- $eq =
- $gt >
- $gte >=
- $lt <
- $lte <=
- $ne !=
- $in valores dentro de Array
- $nin valores NO ...

### Operadores Lógicos
- $and
- $not
- $nor
- $or

### Operadores Por Elemento
- $exists Ver si doc cuenta con campo
- $type Ver que tipo de dato esta guardado en un campo

### Operadores de Arrays
- $all SubQuery a los elementos del Array, trae todos
- $elemMatch SubQuery para los docs y embedded docs del Array
- $size len(array)
- $addToSet Agregar valor al Array
- $pull Eliminar Valores del Array

### Methods de Query
- .skip(int) Se salta los INT primeros valores
- .limit(int) Solo toma los INT primeros Valores

## Agregaciones: Super Query

Las agregaciones son una forma de poder hacer queries super potentes. Teniendo varios 
para diferentes situaciones:

### Pipeline de Agregaciones

Se usa Aggregations más que todo para obtener datos de un grupo de datos, 
como la suma, average o max, min, etc. Creando un grupo con un $match, como tamaño u 
caracteristica general. Para despues agrupar los datos del $match con un $group.
Haciendo que este proceso sea de stages.
Se puede modificar o agregar los datos con $out u $merge, pero no se explica.
Tener varios stages, puede perjudicar el performance del Query.

### Map-Reduce

Map-Reduce es Depreciado, Degradado, Olvidado, lo mejor es no explicarlo y usarlo.

### Otras functions

- count() y estimatedDocumentCount():
	Es una forma de contar todos los docs de una collection, solo que cambia su velocidad y 
	resultado una vez la collection tenga muchisimos docs registrados.
	
- distinct(field):
	Nos devuelve un Array de los valores posibles dentro de los docs de la collection de un field.

# El Proyecto Mongo Platzi

El proyecto lo vamos a hacer usando Python y Flask, vamos a hacer una API para nuestra DB. Vamos a usar esta con 
Postman, que es una herramienta para usar de mejor forma las APIs.

Podemos instalar Postman desde el AUR, aunque me salio un error al iniciar despues de configurar todo, lo configure y 
al parecer todo esta bien?

Para python simplemente vamos a hacer un clone de un código ya hecho, aunque me gustaría mejorar y hacer otro directamente para 
el proyecto del curso. Solo es clone, y pip a los requirements. Exportamos las variables de Flask y listo.
Hice un script para que esto no fuera cada vez que quiera iniciar el server desde 0.

He encontrado varios errores que practicamente son de los 3 años que han acurrido desde el curso. Principalmente cambios a 
la forma de como se usa pymongo. Creo que lo mejor es hacer yo mismo un API usando Flask para que no sea tan dificil volver a 
hacer todo el proyecto. Aunque podría rehacerlo, y ponerlo cómo aporte de Platzi, para que no se confundan tanto las personas.

He vuelto, despues de un hiatus extremo por examenes. He logrado probar y usar la DB desde la app de Flask, estoy mirando las posibles
opciones y methods de Pymongo y estruturado la forma que va a tener la API.
