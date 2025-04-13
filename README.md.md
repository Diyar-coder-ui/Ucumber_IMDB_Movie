
# Ucumber_IMDB_Movie - Movie Recommender System

This project is a simple AI-powered movie recommendation system using cosine similarity and a basic GUI built with Tkinter. The system suggests movies based on text similarity between movie overviews.

## Features
- GUI built with Tkinter
- Cosine similarity from movie overviews
- Based on IMDb-style CSV input
- Scrollable recommendation output

## Instructions

1. Make sure you have Python installed (preferably 3.8+).
2. Install required libraries:
   ```bash
   pip install pandas scikit-learn
   ```
   > `tkinter` is included by default in most Python distributions.
3. Run the script:
   ```bash
   python movie_recommender.py
   ```
4. In the GUI, enter a movie title like `"Inception"` to receive recommendations.

## Files

- `movie_recommender.py`: Main Python code for GUI and logic
- `movies.csv`: Dataset with movie titles and descriptions
- `README.txt`: These setup instructions

## Notes

- Current dataset is limited to 5 movies. You can expand `movies.csv` to improve recommendation quality.
- All computation is done locally — no data is collected or transmitted.

## Author

Asfandiyar.  
MSAI 631 — University of the Cumberlands
