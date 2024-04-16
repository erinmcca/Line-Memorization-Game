# Line-Memorization-Game
A text-based game to help actors memorize their lines from a play script. 

AKA: Hi Andrew I am so sorry for giving you so many lines to learn, please accept my gift of atonement. 

## Current status
Start by selecting a character to review the lines of. The file automatically runs 50 rounds of the game, which presents you with a preceding line or stage direction, prompts you to enter the character's line that comes next, lets you see the first two words of the line if you type !hint, and gives you a score using the Levenshtein distance between your answer and the actual line. 
You have the option to either go through all lines randomly, or to start with a specific scene. 

## To-dos
A lot. 

Scoring could factor in semantic distance (word2vec or similar) as well. 

Keep track of scores to know which lines the user struggles with the most. 

Somehow predict even before the game is played which lines will be the most difficult based on things like length and word rarity. 

Let you choose whether you want to do all in order, do a specific scene or set of scenes, do completely random, or do only a certain number of the lowest scoring lines. 
UPDATE: Some of these have been implemented but not as thoroughly as I'd like. 

Or only preceding lines from certain characters, if you happen to prefer running lines with other actors but there are some you can't get a hold of as easily. 

Different difficulty modes- flashcards, multiple choice, fill in the blank, fill in all blanks (you still have to type the whole thing but you see beforehand how many sentences there are, how long the words are, how many words in each sentence). 

Different amounts revealed by hints. 

Etc. 
