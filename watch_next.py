
import spacy

# Function to read txt file
def read_file(file_name):

    with open(file_name,'r') as f:
        for line in f:
            line = line.replace("\n","")
            movie_descriptions.append(line)

# Function to reccomend movie with most similar description
def recommend(model_sentence): 
    # Values to store most similar description
    recommendation = None   
    most_similar = 0

    for description in movie_descriptions:
        # Stplitting string by : to seperate description
        description = description.split(":")
        # Passing description only by index
        similarity = nlp(description[1]).similarity(model_sentence)

        if similarity > most_similar:
            most_similar = similarity
            recommendation = description

    return recommendation

nlp = spacy.load('en_core_web_md')

# list to store list of descriptions
movie_descriptions =  []

# Description to compare 
description_to_compare = """Will he save 
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

model_sentence = nlp(description_to_compare)

read_file('movies.txt')

# Returns list['movie name','description']
test = recommend(model_sentence)

print(f"Movie recomended: {test[0]}")
print(f"Description: {test[1]}")