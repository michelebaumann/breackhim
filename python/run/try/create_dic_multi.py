from itertools import product
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor


print("Dictionary creation started")

current_folder = os.getcwd()

# Delete existing dictionary.txt if it exists
dictionary_path = os.path.join(current_folder, 'python', 'lists', 'dictionary.txt')
if os.path.exists(dictionary_path):
    os.remove(dictionary_path)

def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def create_dictionary(event, partner, game, date):
    all_lists = [event, partner, game, date]
    total_elements = len(event) * len(partner) * len(game) * len(date)
    progress_bar = tqdm(total=total_elements, desc="Creating dictionary", unit="pair")
    pairs_set = set()

    def add_pairs(i):
        for pair in product(all_lists[i], *(all_lists[:i] + all_lists[i+1:])):
            pairs_set.add(f"{pair[0]}_{pair[1]}")
            progress_bar.update()

    with ThreadPoolExecutor() as executor:
        executor.map(add_pairs, range(len(all_lists)))

    progress_bar.close()
    return pairs_set

def save_dictionary_to_file(dictionary, file_path):
    with open(file_path, 'w') as file:
        for item in dictionary:
            file.write(item + '\n')

event = list(set(read_words_from_file(os.path.join(current_folder, 'python', 'lists', 'leet', 'event.txt'))))
partner = list(set(read_words_from_file(os.path.join(current_folder, 'python', 'lists', 'leet', 'partner.txt'))))
game = list(set(read_words_from_file(os.path.join(current_folder, 'python', 'lists', 'leet', 'game.txt'))))
date = list(set(read_words_from_file(os.path.join(current_folder, 'python', 'lists', 'leet', 'date.txt'))))

dictionary = create_dictionary(event, partner, game, date)
os.makedirs(os.path.dirname(os.path.join(current_folder, 'python', 'lists', 'dictionary.txt')), exist_ok=True)
save_dictionary_to_file(dictionary, os.path.join(current_folder, 'python', 'lists', 'dictionary.txt'))
print("Dictionary creation completed")