# Word-Blitz
A mixture of Hangman and Wheel of fortune either against another player, or the computer. A list of puzzles is loaded into the game via reading the supplied textfile. In which there are a list of clues and words.
This is a two player game - ask each of the players what their names are. Once the game begins, players are presented with the puzzle category as a hint but the individual letters are replaced by placeholders (dashes or underscores). For instance, the secret word in the following example is professor. The players are presented with the category, occupation, and nine blank spaces which represent each of the letters that occur in the secret string (professor).

Category: Occupation                                                 Secret Word: _ _ _ _ _ _ _ _ _                  Guessed Letters: 

Players can guess either consonants or vowels. If a player wishes to guess a consonant, they must spin the wheel. Vowels, on the other hand, can be purchased for $25 a piece.

Suppose I guess the letter "O". The interface would be updated like so:

Category: Occupation                                                 Secret Word: _ _ O _ _ _ _ O _                 Guessed Letters: O

Once my turn is finished, it would be the next player's (or the computer's) chance to guess a letter. 

Turns:
At each turn, the player has the following options:

1) quit the game
2) solve the puzzle
3) spin the wheel 
4) buy a vowel

If the player decides to solve the puzzle and are correct, they are awarded 5$ per word that had not been unveiled before


If the player decides to spin the wheel, the following will happen:

If the spin results in a 0, this is the bankruptcy element - the player's turn money is reset to zero and the player’s turn is over.

If the spin results in a 21, this is the lose-a-turn element - the current player's turn ends.

If the spin results in a dollar amount (any number other than 0 or 21), the player is allowed to choose a consonant. The player is immediately asked to enter the consonant that they would like to purchase.

Players can also buy a vowel for a flat fee of 25$ which will be deducted from their balance
