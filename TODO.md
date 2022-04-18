# Find word
A simple game to find a word that has 5 letters.

# Requirements
- The game selects a word with 5 letters
- You can enter a guess word with 5 letters
- The game tells you which letters exits and if they are in the right position

Ex:
The word is: KNIFE

First guess: NIGHT

Game returns:
  - Doesn't have: G, H, T
  - Have in a different position: N, I
  - Have in the right position:


# TODOS:
- Setup a python project #DONE
- Store a list of words with 5 letters #DONE
- Word abstraction with some way to know the letter position #DONE
- Validate the entered word
  - has 5 letters #DONE
  - the entered word is a valid word: exists in our list of words
- Compare word with another, and return the differences 
- Indifference with words that has accent
