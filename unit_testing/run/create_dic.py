from itertools import product
import os
from tqdm import tqdm

print("Dictionary creation started")

current_folder = os.getcwd()

# Delete existing dictionary.txt if it exists
dictionary_path = os.path.join(current_folder, 'unit_testing', 'lists', 'raw', 'dictionary.txt')
if os.path.exists(dictionary_path):
    os.remove(dictionary_path)

def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def create_dictionary(event, partner, game, date):
    all_lists = [event, partner, game, date]
    total_elements = sum(len(lst) * len(lst2) for lst in all_lists for lst2 in all_lists if lst is not lst2)
    progress_bar = tqdm(total=total_elements, desc="Creating dictionary", unit="pair")
    pairs_set = set()
    for lst in all_lists:
        for lst2 in all_lists:
            if lst is lst2:
                continue
            for pair in product(lst, lst2):
                if pair[0] != pair[1]:
                    pairs_set.add('_'.join(pair))
                    progress_bar.update()
    progress_bar.close()
    return pairs_set

def save_dictionary_to_file(dictionary, file_path):
    with open(file_path, 'w') as file:
        for item in tqdm(dictionary, desc="Saving words"):
            file.write(item + '\n')

event = list(set(read_words_from_file(os.path.join(current_folder, 'unit_testing', 'lists', 'raw', 'event.txt'))))
partner = list(set(read_words_from_file(os.path.join(current_folder, 'unit_testing', 'lists', 'raw', 'partner.txt'))))
game = list(set(read_words_from_file(os.path.join(current_folder, 'unit_testing', 'lists', 'raw', 'game.txt'))))
date = list(set(read_words_from_file(os.path.join(current_folder, 'unit_testing', 'lists', 'raw', 'date.txt'))))

dictionary = create_dictionary(event, partner, game, date)
os.makedirs(os.path.dirname(os.path.join(current_folder, 'unit_testing', 'lists', 'raw' 'dictionary.txt')), exist_ok=True)
save_dictionary_to_file(dictionary, os.path.join(current_folder, 'unit_testing', 'lists', 'raw', 'dictionary.txt'))
print("Dictionary creation completed")