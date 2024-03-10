import itertools
import os
from tqdm import tqdm

current_folder = os.getcwd()

# Leet mapping dictionary
leet_mapping = {
    'a': ['a', 'A', '4'],
    'b': ['b', 'B', '8'],
    'c': ['c', 'C'],
    'd': ['d', 'D'],
    'e': ['e', 'E', '3'],
    'f': ['f', 'F'],
    'g': ['g', 'G', '9'],
    'h': ['h', 'H'],
    'i': ['i', 'I', '1'],
    'j': ['j', 'J'],
    'k': ['k', 'K'],
    'l': ['l', 'L', '1'],
    'm': ['m', 'M'],
    'n': ['n', 'N'],
    'o': ['o', 'O', '0'],
    'p': ['p', 'P'],
    'q': ['q', 'Q'],
    'r': ['r', 'R'],
    's': ['s', 'S', '5'],
    't': ['t', 'T', '7'],
    'u': ['u', 'U'],
    'v': ['v', 'V'],
    'w': ['w', 'W'],
    'x': ['x', 'X'],
    'y': ['y', 'Y'],
    'z': ['z', 'Z'],
}


def generate_combinations(word):
    # Generate all combinations of leet mapping
    leet_letters = [leet_mapping.get(c, [c]) for c in word]
    combinations = set()
    for leet_combination in tqdm(itertools.product(*leet_letters), desc=f"Generating combinations for {word}", unit="combination"):
        combinations.add(''.join(leet_combination))
    return combinations

word_files = [current_folder+'/lists/raw/date.txt', current_folder+'/lists/raw/event.txt', current_folder+'/lists/raw/game.txt', current_folder+'/lists/raw/partner.txt']

# Read words from each file
for file in tqdm(word_files, desc="Processing files", unit="file"):
    with open(file, 'r') as f:
        words = [line.strip() for line in f]

    # Generate all combinations for each word
    all_combinations = [generate_combinations(word) for word in tqdm(words, desc=f"Generating combinations for {file}", unit="word")]

    # Create a new file in the specified directory
    base = os.path.basename(file)
    new_file = os.path.join(current_folder, 'lists', 'leet', base)
    with open(new_file, 'w') as f:
        # Write all combinations to the new file
        for word_combinations in tqdm(all_combinations, desc=f"Writing to {new_file}", unit="combination"):
            for combination in word_combinations:
                f.write(combination + '\n')

print("Leet creation completed.")