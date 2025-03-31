from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# Downloading imdb top 250 movie's data
url = 'https://www.imdb.com/chart/top/'

# Headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Make the request with headers
response = requests.get(url, headers=headers)

# Check response
print(response.status_code)  

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.select('h3.ipc-title__text')
ratings = [rating.get_text(strip=True) for rating in soup.select('span.ipc-rating-star--rating')]
print(len(ratings))



# create a empty list for storing
# movie information
list = []

# Iterating over movies to extract
# each movie's details

for index in range(min(len(movies), len(ratings))):  
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    
    data = {
        "movie_title": movie_title,
        "rating": ratings[index] if index < len(ratings) else "N/A",  
    }

    
    list.append(data)


# printing movie details with its rating.
for movie in list:
	print(movie['movie_title'], movie['rating'])


##.......##
df = pd.DataFrame(list)
df.to_csv('imdb_top_250_movies.csv',index=False)