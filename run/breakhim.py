from itertools import product
from string import ascii_lowercase
from zipfile import ZipFile
import os

import concurrent.futures

current_folder = os.getcwd()
zip_file_paths = [current_folder+'/zips/breakme_giovanni_1.zip',current_folder+'/zips/breakme_giovanni_2.zip',current_folder+'/zips/breakme_giovanni_3.zip',current_folder+'/zips/breakme_giovanni_4.zip']
dictionary = current_folder+'/lists/dictionary.txt'
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

def process_zip_file(args):
    zip_file_path, dictionary = args
    if not os.path.exists(zip_file_path):
        print(f"File {os.path.basename(zip_file_path)} does not exist.")
        return
    print(f"Brute forcing {os.path.basename(zip_file_path)}...")
    for password in dictionary:
        if bruteforce_zip_password(zip_file_path, password) is not None:
            print(f"Found password for {os.path.basename(zip_file_path)}: {password}")
            break

if __name__ == '__main__':
    dictionary = read_dictionary_file(current_folder+'/lists/dictionary.txt')
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_zip_file, [(path, dictionary) for path in zip_file_paths])