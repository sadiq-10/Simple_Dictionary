import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        valid = input(f"Did you mean %s instead of {w}. Please write Y for yes and N for no." %get_close_matches(w, data.keys())[0])
        if valid == "Y":
            return get_close_matches(w, data.keys())[0]
        elif valid == "N":
            return "We can't understand you."
        else:
            return "Try a valid word"
    else:
        return "You inseted an invalid word.."


user_word = input("Write a word: ")
output = translate(user_word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)