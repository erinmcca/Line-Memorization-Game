# line memorization game
# most basic form- just get setanta's lines from cu chulainn script
# paired with preceeding line


import random
import Levenshtein
import re


#script = open("Cu Chulainn Script (With Cuts).txt", 'r')


with open("Cu Chulainn Script (With Cuts).txt", 'r', encoding="utf8") as script:
    

    #print(script.readline())


    lines = script.readlines()
    #print(type(lines))
    #print(lines[:20])


def get_setanta_lines():
    # there will be a more general one where the character is an argument

    #with open("Setanta Lines.txt", "w") as line_file:

    setanta_lines = []

    for i in range(len((lines))):
        if(lines[i] == 'SETANTA\n'):
            setanta_lines.append(lines[i+1])
                #line_file.write(lines[i+1])

    #print(len(setanta_lines))
    return setanta_lines


def make_line_mem_game(lines, char_lines):
    # for every line in the file get the one before it
    # then dictionary i guess
    # json format?
    # take lines as a list at least for now

    #line_and_prev = {}
    pairs = []

    lines.remove("\n") # how to remove all instances???

    for line in char_lines:
        i = lines.index(line)

        if(line != lines[i]):
            print("something went wrong....")
            break
        
        prev_line = lines[i-4]

        #line_and_prev[line] = prev_line
        pair = (prev_line, line)
        pairs.append(pair)


    #return line_and_prev
    return pairs


def run_game(rounds, pairs):
    count = 0
    print("Type !hint for the first two words")
    while count <= rounds:
        r = random.randint(1, len(pairs)-1)
        pair = pairs[r]
        prev_line = pair[0]
        true_line = pair[1]
        #true_line = re.sub(r"[\n\t]*", "", true_line)
        true_line = " ".join(true_line.split())
        print(prev_line)
        your_line = input("Type your line that comes after this: ")
        if(your_line=="!hint"):
            print(true_line.split(" ")[:2])
            your_line = input()

        # have a way to grade the answer
        # probably levenshtein distance
        # also factoring in semantic difference would be ideal

        grade = Levenshtein.ratio(your_line.lower(), true_line.lower())
            
        print(f'That was {grade}% correct!')
        print("The line is actually:")
        print(true_line)

        count += 1



setanta_lines = get_setanta_lines()

pairs = make_line_mem_game(lines, setanta_lines)

print(pairs[:5])

#print(list(pairs.keys())[:5])
#print(list(pairs.values())[:5])

run_game(5, pairs)
    
