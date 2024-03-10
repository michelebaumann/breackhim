from itertools import product
import os

current_folder = os.getcwd()

def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def create_dictionary(event, partner, game, date):
    all_lists = [event, partner, game, date]
    for i in range(len(all_lists)):
        for pair in product(all_lists[i], *(all_lists[:i] + all_lists[i+1:])):
            yield f"{pair[0]}_{pair[1]}"

def save_dictionary_to_file(dictionary, file_path):
    with open(file_path, 'w') as file:
        for item in dictionary:
            file.write(item + '\n')

event = read_words_from_file(current_folder+'/lists/leet/event.txt')
partner = read_words_from_file(current_folder+'/lists/leet/partner.txt')
game = read_words_from_file(current_folder+'/lists/leet/game.txt')
date = read_words_from_file(current_folder+'/lists/leet/date.txt')

dictionary = create_dictionary(event, partner, game, date)
print(os.path.abspath(current_folder+'/lists/dictionary.txt'))
os.makedirs(os.path.dirname(current_folder+'/lists/dictionary.txt'), exist_ok=True)
save_dictionary_to_file(dictionary, current_folder+'/lists/dictionary.txt')