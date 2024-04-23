# CHALLENGE #1

[michelebaumann/breakhim](/)

## general

```python
#path
current_folder = os.getcwd()

dictionary_path = os.path.join(current_folder, 'python', 'lists', 'raw', 'dictionary.txt')
#current_folder/python/lists/raw/dictionary.txt

#progress bar
progress_bar = tqdm(total=total_elements, desc="Creating dictionary", unit="pair")
```

## .txt and .zip

1. .txt

```python
def create_dictionary(event, partner, game, date):
    all_lists = [event, partner, game, date]
    ...
    return pairs_set
    #pairs_set : set

event = list(set(read_words_from_file(os.path.join(current_folder, 'python', 'lists', 'raw', 'event.txt'))))

dictionary = create_dictionary(event, partner, game, date)
os.makedirs(os.path.dirname(os.path.join(current_folder, 'python', 'lists', 'raw' 'dictionary.txt')), exist_ok=True)
```

1. .zip

```python
def bruteforce_zip_password(zip_file_path, password):
    with ZipFile(zip_file_path, 'r') as zip_file:
        try:
            zip_file.extractall(pwd=bytes(password, 'utf-8'))
            return password
        except:
            return None
```
