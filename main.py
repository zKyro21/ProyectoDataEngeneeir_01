from fastapi import FastAPI
import pandas as pd

df_plt = pd.read_csv('https://raw.githubusercontent.com/zKyro21/Dataset-Proyecto/main/plataformas.csv?token=GHSAT0AAAAAAB5ROUSVMS2LSYRZLZIIWI26Y6JVTIA')

app = FastAPI()

@app.get('/')
async def index():
    return 'Hola mundo, Inicio de la API'

#Conteo de palabras dependiendo la plataforma y palabra en cuestion a buscar
@app.get('/count-keyword')
async def conteo(platform: str, keyword: str):
    mask = (df_plt['streaming_service'] == platform) & (df_plt['title'].str.contains(keyword))
    return ('Plataforma: '+ platform , keyword + ': ' + str(len(df_plt[mask])))

#Buscar y contar peliculas siendo mayor a cierto puntaje y año epecifico
@app.get('/count-score')
async def count_puntaje(platform: str, score: int, year: int):
    mask = (df_plt['streaming_service'] == platform) & (df_plt['score'] > score) & (df_plt['release_year'] == year)
    return ('Plataforma: '+ platform, 'Puntaje mayor a ' + str(score), 'Año de salida: ' + str(year), 'Cantidad: ' + str(len(df_plt[mask])))

#Segunda pelicula con mayor score en base a la plataforma y ordenada de forma alafabetica
@app.get('/second_score')
async def second_score(plataforma: str):
    mask = df_plt['streaming_service'] == plataforma
    df_plt.sort_values(by= ['score','title'], ascending= [False,True], inplace= True)
    return (df_plt[mask].iloc[1]['title'], 'Score: ' + str(df_plt[mask].iloc[1]['score']))

#Busqueda de dato mas largo en base a los argumentos de año, plataforma y tipo de duracion
@app.get('/longer-movie')
async def longer_movie(plataform: str, dur_type: str, year: int):
    mask = (df_plt['release_year'] == year) & (df_plt['streaming_service'] == plataform) & (df_plt['duration_type'] == dur_type)
    df_plt[mask].sort_values(by= 'duration_int', ascending= False)
    lm = df_plt[mask].sort_values(by= 'duration_int', ascending= False).iloc[0]
    return (lm['title']+' '+ str(lm['duration_int'])+' '+ lm['duration_type'])

#Contar la cantidad de elementos con un raiting especifico
@app.get('/count-rating')
async def count_rating(rating: str):
    mask = df_plt['rating'] == rating
    return ('Rating: '+ rating, 'Cantidad: ' + str(len(df_plt[mask])))