from database import find_words
import json

# ..source: https://www.geeksforgeeks.org/
# ..    reading-and-writing-json-to-a-file-in-python/
def covert_to_json():
    list_of_words = list()

    for word in find_words():
        list_of_words.append(word["word"])
    dictionary = {"words": list_of_words}

    with open("sample.json", "w") as outfile:
        json.dump(dictionary, outfile)
