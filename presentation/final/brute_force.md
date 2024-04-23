# CHALLENGE #1

[michelebaumann/breakhim](/)

## brute force

```python
current_folder = os.getcwd()
zip_file_paths = [
    os.path.join(current_folder, 'python', 'zips', 'breakme_giovanni_1.zip'),
    os.path.join(current_folder, 'python', 'zips', 'breakme_giovanni_2.zip'),
    os.path.join(current_folder, 'python', 'zips', 'breakme_giovanni_3.zip'),
    os.path.join(current_folder, 'python', 'zips', 'breakme_giovanni_4.zip')
]
dictionary = os.path.join(current_folder, 'python', 'lists', 'dictionary.txt')

def bruteforce_zip_password(zip_file_path, password):
    with ZipFile(zip_file_path, 'r') as zip_file:
        try:
            zip_file.extractall(pwd=bytes(password, 'utf-8'))
            return password
        except:
            return None

def read_dictionary_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

if __name__ == '__main__':
    print("Starting brute force attack...")
    ...
    print("Brute force completed.")
```
