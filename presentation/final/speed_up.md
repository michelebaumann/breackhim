# CHALLENGE #1

[michelebaumann/breakhim](/)

## speed-up

**1. Change sequence of code**

1. Leet combinations and then combine words.
   Combine words took way **loooonger** than leet combinations.
   Saving words to .txt file took more time so I adjusted.
2. Combine words and then leet combinations **(and screw up while change code)**.

**2. Just make it faster**

1. Different data structure **(hell no)**.
2. Make it parallel.
   1. Multiple threads
   - In Python, due to the Global Interpreter Lock (GIL), multiple threads don't actually run in true parallel on multiple cores. Code in **C** or **C#** **(hell no)**.
   - In this case, since the task is **CPU-bound (trying different passwords to unzip a file)**, using threads in Python won't speed up the code.
   2. Multiple process
   - `concurrent.futures.ProcessPoolExecutor` runs each task (brute force .zip file) in a separate process and can therefore utilize multiple cores **(hell yess)**.

```python
def bruteforce_zip_password(zip_file_path, password):
    ...

def read_dictionary_file(file_path):
    ...

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
```
