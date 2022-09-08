# Curso Básico de Mondongo DB

Gooddamit, no tengo las skills de Backend con APIs para este curso, lo mejor es 
volver cuando las sepa. hoy 06/06/22. Escribire cuando vuelva.

Hello. Dios, ha sido tanto tanto tiempo, me da melancolía volver por acá.
Han pasado exactamente 2 meses desde que deje este mensaje. Hoy 08/06/2022 vuelvo 
a retomar mi ruta de aprendizaje.

start: 08/06/2022
end: 

sessions:
1. 08/06/2022: ... - 20:18

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
