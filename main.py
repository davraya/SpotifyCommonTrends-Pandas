import pandas as pd


# popularity is based on how much a song has been played recently. 

df = pd.read_csv("unpopular_songs.csv") # creates a DataFrame()

number_of_songs = df.index.stop

def get_elements_in_range(column_name, start, multiplicator=0.1, end=1):
    lower_limit_elements = df[df[column_name] < multiplicator * start]
    upper_limit_elements = df[df[column_name] < multiplicator * (start + end)]

    elements_in_range = len(upper_limit_elements) - len(lower_limit_elements)

    return(f"The number of songs with a {column_name} between {start} and {start + 1} is {elements_in_range}")

danceability = [get_elements_in_range("danceability", start) for start in range(10)]
print(*danceability, sep='\n')
print()
danceability = [get_elements_in_range("energy", start) for start in range(10)]
print(*danceability, sep='\n')
print()
danceability = [get_elements_in_range("speechiness", start) for start in range(10)]
print(*danceability, sep='\n')
print()
danceability = [get_elements_in_range("loudness",start) for start in range(-52, 5, 1)]
print(*danceability, sep='\n')
print()

keys_count = df["key"].value_counts() # number of each entry for a column
keys = ["C", "C#/D♭", "D", "D#/E♭", "E", "F", "F#/G♭", "G", "G#/A♭", "A", "A#/B♭", "B"]
i = keys_count.idxmax()

print(f"\nThe number of songs is: {number_of_songs}")
print(f"Common trends among unpopular songs\n")
print(f"1. The most common music key among unpopular songs is {keys[i]}")
print(f"2. Danceability describes how suitable a track is for dancing. The most common level of danceability is between 6 and 7 (range: 0 - 10)")
print(f"3. Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. The most common energy level is between 5 and 7 (range: 0 - 10)")
print(f"4. The overall loudness of a track in decibels (dB). The most common loudness level is between -52 and -51 db (range: -52 db to 5 db)")
