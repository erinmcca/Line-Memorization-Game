# line memorization game
# most basic form- just get setanta's lines from cu chulainn script
# paired with preceeding line


import random
import Levenshtein
import re


#script = open("Cu Chulainn Script (With Cuts).txt", 'r')


with open("Cu Chulainn Script (With Cuts).txt", 'r', encoding="utf8") as script:
    

    #print(script.readline())


    all_lines = script.readlines() # TODO get rid of all empty newlines
    #print(type(lines))
    #print(lines[:20])

def scene_select(lines, start=["ACT ONE\n", "Scene 1\n"]):
    start_index = lines.index(start[0])
    lines = lines[start_index:]
    start_index = lines.index(start[1])
    lines = lines[start_index:]

    return lines


def get_setanta_lines(lines):
    # there will be a more general one where the character is an argument

    #with open("Setanta Lines.txt", "w") as line_file:

    setanta_lines = []

    for i in range(len((lines))):
        if(lines[i] == 'SETANTA\n'):
            setanta_lines.append(lines[i+1])
                #line_file.write(lines[i+1])

    #print(len(setanta_lines))
    return setanta_lines


# maybe... in random mode, shuffle then go in order
# for starting from a certain scene just delete everything prior
# to differentiate acts, for act 2 first delete the first act then
# delete prior scenes
# that also needs to be done with char lines
# so char lines should be made from modified lines list


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


def run_game(rounds, pairs, randomness=True):
    count = 0
    print("Type !hint for the first two words")
    while count <= rounds:

        if(randomness):
            r = random.randint(1, len(pairs)-1)
        else:
            r = count
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

        grade = 100 * Levenshtein.ratio(your_line.lower(), true_line.lower())
            
        print(f'That was {grade}% correct!')
        print("The line is actually:")
        print(true_line)
        print("\n")

        count += 1

     
#start = ["ACT ONE\n", "Scene 3\n"]

randomness = False

custom = input("Do you wish to select a specific scene? Type y or n.")
if(custom=="y"):
    actnum = input("Which act? Type 1 or 2")
    act = "ACT ONE\n"
    match actnum:
        case "1":
            act = "ACT ONE\n"
        case "2":
            act = "ACT TWO \n" # whyyyyy is the formatting inconsistent
        case _:
            print("There's only 2 acts. I mean.... Unless you count the stuff with Fand... But I haven't written that yet.\n We're going with Act 1.")
    scenenum = input("Which scene? Type a number from 1 to 8.")
    scene = f'Scene {scenenum}\n'
    start = [act, scene]

else:
    start=["ACT ONE\n", "Scene 1\n"]
    randomness = True

lines = scene_select(all_lines, start)

setanta_lines = get_setanta_lines(lines)

pairs = make_line_mem_game(lines, setanta_lines)

#print(pairs[:5])

#print(list(pairs.keys())[:5])
#print(list(pairs.values())[:5])

run_game(50, pairs, randomness)
    
