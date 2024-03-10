import cProfile
from itertools import product
import os

def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def create_dictionary(event, partner, game, date):
    all_lists = [event, partner, game, date]
    return [f"{pair[0]}_{pair[1]}" for i in range(len(all_lists)) for pair in product(all_lists[i], *(all_lists[:i] + all_lists[i+1:]))]

def save_dictionary_to_file(dictionary, file_path):
    with open(file_path, 'w') as file:
        file.write('\n'.join(dictionary))

def main():
    current_folder = os.getcwd()
    event = read_words_from_file(current_folder+'/lists/leet/event.txt')
    partner = read_words_from_file(current_folder+'/lists/leet/partner.txt')
    game = read_words_from_file(current_folder+'/lists/leet/game.txt')
    date = read_words_from_file(current_folder+'/lists/leet/date.txt')

    dictionary = create_dictionary(event, partner, game, date)
    save_dictionary_to_file(dictionary, current_folder+'/lists/dictionary.txt')

cProfile.run('main()')