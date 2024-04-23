# CHALLENGE #1

[michelebaumann/breakhim](/)

## leet mapping

**(Note that every "word" may -or may not- be spelled in w3irD ways...)**

**Leet or "1337"**

```python
leet_mapping = {
     'a': ['a', 'A', '4', '@'],
     'b': ['b', 'B', '8', '6'],
     'c': ['c', 'C'],
     'd': ['d', 'D',],
     'e': ['e', 'E', '3', '€', '£'],
     'f': ['f', 'F', '7'],
     'g': ['g', 'G', '9', '6'],
     'h': ['h', 'H'],
     'i': ['i', 'I', '1'],
     'j': ['j', 'J'],
     'k': ['k', 'K'],
     'l': ['l', 'L', '1'],
     'm': ['m', 'M'],
     'n': ['n', 'N'],
     'o': ['o', 'O', '0'],
     'p': ['p', 'P'],
     'q': ['q', 'Q', '9'],
     'r': ['r', 'R'],
     's': ['s', 'S', '5', '$'],
     't': ['t', 'T', '7', '+'],
     'u': ['u', 'U'],
     'v': ['v', 'V'],
     'w': ['w', 'W'],
     'x': ['x', 'X'],
     'y': ['y', 'Y'],
     'z': ['z', 'Z', '2', '7', '5'],
}
```

All words in lowercase letters

## code

```python
def generate_combinations(word):
    # Generate all combinations of leet mapping
    leet_letters = [leet_mapping.get(c, [c]) for c in word]
    combinations = set()
    for leet_combination in itertools.product(*leet_letters):
        combinations.add(''.join(leet_combination))
    return combinations

word_files = [
    os.path.join(current_folder, 'python', 'lists', 'raw', 'dictionary.txt')
]

# Read words from each file
for file in word_files:
    with open(file, 'r') as f:
        words = [line.strip() for line in f]

    print("generating combinations started")
    # Generate all combinations for each word
    all_combinations = []
    for word in tqdm(words, desc="Processing words", unit="word"):
        all_combinations.append(generate_combinations(word))
    print("generating combinations completed")

    # Create a new file in the specified directory
    print("writing to file started")
    base = os.path.basename(file)
    new_file = os.path.join(current_folder,'python', 'lists', base)
    with open(new_file, 'w') as f:
        # Write all combinations to the new file
        for word_combinations in all_combinations:
            for combination in word_combinations:
                f.write(combination + '\n')
    print("writing to file completed")

print("Leet creation completed.")
```
