from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

movies = [
    {"title": "Inception", "genre": "sci-fi thriller"},
    {"title": "Titanic", "genre": "romance drama"},
    {"title": "Interstellar", "genre": "sci-fi space"},
    {"title": "The Notebook", "genre": "romance love"},
    {"title": "Avengers", "genre": "action superhero"}
]

genres = [movie["genre"] for movie in movies]

vectorizer = CountVectorizer().fit_transform(genres)
similarity = cosine_similarity(vectorizer)

def recommend(movie_name):
    movie_index = None
    for i, movie in enumerate(movies):
        if movie["title"].lower() == movie_name.lower():
            movie_index = i
            break

    if movie_index is None:
        print("Movie not found")
        return

    scores = list(enumerate(similarity[movie_index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:3]

    print("Recommended movies:")
    for i in scores:
        print(movies[i[0]]["title"])

user_input = input("Enter a movie name: ")
recommend(user_input)
