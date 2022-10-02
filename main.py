import pandas as pd



# This creates a pandas.DataFrame
df = pd.read_csv("unpopular_songs.csv")

# the numbe of rows in the DataFrame
number_of_songs = df.index.stop

"""
Get elements in Range:
    The purpose of this function is to take a pandas.Series
    and basically take and create subseries based on a range
    of values and return the size of such subserie. 
"""
def get_elements_in_range(column_name, start, multiplicator=0.1, end=1):
    # Reducing the subserie to just the lower part of the start
    lower_limit_elements = df[df[column_name] < multiplicator * start]
    # Reducing the subserie to just the uppe limit
    upper_limit_elements = df[df[column_name] < multiplicator * (start + end)]

    # Example: If we have a Serie with possible numbers (Each value will most likley be 
    # unique with decimal numbers) with between 1 and 10 and we want to know how
    # many elements have a value between 3 and 4 we will first count all the values 
    # from 1 to 3 (lower limmit count) then we will count all the values form 1 to 4 (upper limit count).
    # Then we simply subtract lower limit count from the upper limit count. 
      
    
    elements_in_range = len(upper_limit_elements) - len(lower_limit_elements)

    return(f"The number of songs with a {column_name} between {start} and {start + 1} is {elements_in_range}")


# Here I use list comprehension 
danceability = [get_elements_in_range("danceability", start) for start in range(10)]
# The * is called the unpack operator
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
