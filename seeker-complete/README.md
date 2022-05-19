# Seeker
Experience the thrill of the chase! <i>Seeker</i> might seem easy but even the best get lost 
from time to time. The rules are simple. The seeker guesses the hider's location and the hider 
provides a hint - that's confidence! Guessing continues until the hider is found.

---
## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 seeker 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- seeker              (source code for game)
  +-- game              (specific classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0

## Authors
* Matt Manley (manleym@byui.edu)
* Scott Burton (burtons@byui.edu)

- kelley will create the repository

- send kelley a link for adding people to repo

list of words, pick one at random, start hangman

everyone- Director: handles the game itself- here we'll mark the words and replace the dashes by letters or remove the pieces of the parachute.

cristian- Hider: The jumper itself. Here we will use a word list instead of a number range. We will pick one word at random -- here we mark the drawing!

kelley - Seeker: The user will try to guess the word at random letter by letter. We'll import the word, break it down into individual letters, and then check if the user's input matches these.

shanny- Terminal Service: instead of numbers, ensure it updates based on text strings, this reads the input as is then used by director to continue the game.


word from the word list must have the same character count (will make the process easier).

_e___

"drawing" of the parachute should be done by index ("add \ on index[1] for ex), then remove these one by one as they get it wrong

hider

--------
 ___
/___\
\   /
 \ /
  0
 /|\
 / \

^^^^^^^^

