import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import Scrollbar, Text

df = pd.read_csv("movies.csv")
df = df.dropna(subset=["overview"])

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["overview"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df["title"]).drop_duplicates()

def get_recommendations(title):
    if title not in indices:
        return ["Movie not found."]
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df["title"].iloc[movie_indices].tolist()

def show_recommendations():
    movie_title = entry.get()
    recommendations = get_recommendations(movie_title)
    text_box.delete("1.0", tk.END)
    for movie in recommendations:
        text_box.insert(tk.END, movie + "\n")

root = tk.Tk()
root.title("IMDB Movie Recommender")
root.geometry("500x400")

tk.Label(root, text="Enter Movie Title:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack()
tk.Button(root, text="Get Recommendations", command=show_recommendations).pack(pady=10)

scroll = Scrollbar(root)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

text_box = Text(root, height=15, width=60, yscrollcommand=scroll.set)
text_box.pack(padx=10)
scroll.config(command=text_box.yview)

root.mainloop()
