#HOLDEN CORMIER - 05/12/2022
#WORDLE SOLVER

#IMPORTS
import selenium

class WordleSolver:
    words = []
    with open(r'C:\Users\holde\_PersonalProjects\WordleSolver\word_list.txt', 'r') as file:
        for line in file:
            words.append(line.rstrip('\n'))
    print(words)