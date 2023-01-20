## Direccion URL del deploy
https://qabmag.deta.dev/docs

## Funcionamiento

Las consultas realizadas en esta API se basan en mascaras sobre un dataframe con los datos de sobre las plataformas de streaming mas populares para facilitar la busqueda y recaudacion de información de manera especifica.

# Consultas

count-keyword: Conteo de palabras dependiendo la plataforma y palabra en cuestion a buscar

count-score: Buscar y contar peliculas siendo mayor a cierto puntaje y año epecifico

second_score: Segunda pelicula con mayor score en base a la plataforma y ordenada de forma alafabetica

longer-movie: Busqueda de dato mas largo en base a los argumentos de año, plataforma y tipo de duracion

count-rating: Contar la cantidad de elementos con un raiting especifico

# Parametros

Plataforma: Este parametro reduce la busqueda de manera en que te de resultados de una sola plataforma a la vez, es un parametro tipo string y solo aceptara las siguientes opciones
-amazon
-disney
-hulu
-netflix

Keyword: Este parametro es para buscar una palabra especifica en el titulo de las peliculas/series de television, es un parametro tipo string y aceptara cualquier tipo de palabra.

Score: Este parametro es tipo int y obtiene una cantidad con la cual se califican las peliculas y series de television, con esta cantidad se buscaran valores mayores a este.

Year: Este parametro es tipo int y obtiene un numero para reducir la busqueda a el año de salida en especifico de peliculas o series de televisions.

Dur_type: Este parametro tipo string hace referencia al tipo de duracion de peliculas o series, este campo solo acepta las siguientes opciones
-min
-season

Rating: Este parametro tipo string reduce la busqueda en base a la clasificacion de los productos audiovisuales.
