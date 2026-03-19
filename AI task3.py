# Simple Movie Recommendation System with Year

movies = [
    {"name": "Avengers", "genre": "Action", "rating": 8.5, "year": 2019},
    {"name": "John Wick", "genre": "Action", "rating": 8.2, "year": 2014},
    {"name": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "year": 2014},
    {"name": "Matrix", "genre": "Sci-Fi", "rating": 8.7, "year": 1999},
    {"name": "Mr Bean", "genre": "Comedy", "rating": 7.8, "year": 2007},
    {"name": "Hangover", "genre": "Comedy", "rating": 7.7, "year": 2009}
]

print("🎬 Movie Recommendation System")

# User input with validation
while True:
    genre_input = input("Enter genre (Action/Sci-Fi/Comedy): ").strip().lower()
    if genre_input in ["action", "sci-fi", "comedy"]:
        genre = genre_input.title()
        break
    print("Invalid genre. Please enter Action, Sci-Fi, or Comedy.")

while True:
    try:
        min_rating = float(input("Enter minimum rating (1-10): "))
        if 1 <= min_rating <= 10:
            break
        else:
            print("Rating must be between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        min_year = int(input("Enter minimum release year: "))
        if min_year >= 1900:  # Assuming movies from 1900 onwards
            break
        else:
            print("Year must be 1900 or later.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")

print("\n🎯 Recommended Movies:")

found = False

for movie in movies:
    if (movie["genre"] == genre and 
        movie["rating"] >= min_rating and 
        movie["year"] >= min_year):
        
        print(f"{movie['name']} (Rating: {movie['rating']}, Year: {movie['year']})")
        found = True

if not found:
    print("No movies found for your preference.")
