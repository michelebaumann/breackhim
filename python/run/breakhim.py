from itertools import product
from string import ascii_lowercase
from zipfile import ZipFile
import os
from tqdm import tqdm
import concurrent.futures

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

def process_zip_file(zip_file_path, dictionary):
    if not os.path.exists(zip_file_path):
        print(f"File {os.path.basename(zip_file_path)} does not exist.")
        return
    print(f"Brute forcing {os.path.basename(zip_file_path)}...")
    for password in tqdm(dictionary, desc=f"Brute-forcing {os.path.basename(zip_file_path)}", unit="attempt"):
        if bruteforce_zip_password(zip_file_path, password) is not None:
            print(f"Found password for {os.path.basename(zip_file_path)}: {password}")
            break

if __name__ == '__main__':
    print("Starting brute force attack...")
    dictionary = read_dictionary_file(dictionary)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_zip_file, zip_file_paths, [dictionary]*len(zip_file_paths))
    print("Brute force completed.")