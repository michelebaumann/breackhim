import itertools
import os
from tqdm import tqdm

print("Leet creation started")

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
    for leet_combination in itertools.product(*leet_letters):
        combinations.add(''.join(leet_combination))
    return combinations

word_files = [
    os.path.join(current_folder, 'python', 'lists', 'raw', 'date.txt'),
    os.path.join(current_folder, 'python', 'lists', 'raw', 'event.txt'),
    os.path.join(current_folder, 'python', 'lists', 'raw', 'game.txt'),
    os.path.join(current_folder, 'python', 'lists', 'raw', 'partner.txt'),
]

# Read words from each file
for file in word_files:
    with open(file, 'r') as f:
        words = [line.strip() for line in f]

    # Generate all combinations for each word
    all_combinations = [generate_combinations(word) for word in words]

    # Create a new file in the specified directory
    base = os.path.basename(file)
    new_file = os.path.join(current_folder,'python', 'lists', 'leet', base)
    with open(new_file, 'w') as f:
        # Write all combinations to the new file
        with tqdm(total=len(all_combinations), ncols=70) as pbar:
            pbar.set_postfix(file=base, refresh=True)
            for word_combinations in all_combinations:
                for combination in word_combinations:
                    f.write(combination + '\n')
                pbar.update()

print("Leet creation completed.")