import csv
import os

# Define the file path
file_path = '100MostStreamedSongs.csv'

# Read the CSV file
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        artist = row['Artist(s)']  
        song = row['Song']  

        # Create a folder for the artist if it doesn't exist
        artist_folder = os.path.join(os.getcwd(), artist)
        if not os.path.exists(artist_folder):
            os.makedirs(artist_folder)
            print(f"Created folder for artist: {artist}")

        # Create a blank text file for the song in the artist's folder
        song_file = os.path.join(artist_folder, f"{song}.txt")
        if not os.path.exists(song_file):
            open(song_file, 'w').close()
            print(f"Created file for song: {song} by {artist}")

print("All folders and files were created successfully!")
