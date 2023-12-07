from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app=FastAPI()

app.title='Mi app sencillita mi fai'
app.version='0.1.1'

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

@app.get("/" , tags=['home'])
def message():
    return HTMLResponse(content="<h1> mensaje </h1>")

@app.get("/movies" , tags=['movies'])
def get_movies():
    return movies

@app.get("/movies/{id}" , tags=['movies'])
def get_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie

@app.get("/movies/{category}" , tags=['movies'])
def get_movie2(category: str):
    for movie in movies:
        if movie["category"]==category:
            return movie

@app.post("/movies",tags=['movies'])
def create_movie (id: int = Body(),
                  title: str = Body(),
                  overview: str = Body(),
                  year: str = Body(),
                  rating: float = Body(),
                  category: str = Body()):
    movies.append({
        'id':id,
        'title':title,
        'overview':overview,
        'year':year,
        'rating':rating,
        'category':category
    })
    return movies

@app.put("/movies/{id}", tags=['movies'])
def uptade_movie( title: str = Body(),
                  overview: str = Body(),
                  year: str = Body(),
                  rating: float = Body(),
                  category: str = Body()):
    for movie in movies:
        if movie['id']==id:
            movie['title']=title
            movie['overview']=overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category
            break
    return movies

#http://localhost:8000/docs#/movies/get_movie2_movies__category__get
