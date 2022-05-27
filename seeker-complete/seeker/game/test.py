import random

wordlist = ["about", "above", "actor", "acute", "admit"]
word_to_use = random.choice(wordlist)
list_of_letter = list(word_to_use)



print(f"{word_to_use}, {list_of_letter}")

seeker = input("a letter: ")

if seeker in list_of_letter:
    print("Good guess!")
else:
    print("nope")