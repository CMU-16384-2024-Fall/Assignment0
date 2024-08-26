import zipfile
import os

def create_submission():
    with zipfile.ZipFile('handin.zip', 'w') as zf:
        zf.write('ex1.py')
        zf.write('ex2.py')
        zf.write('ex3.py')
    print("Created submission archive: handin.zip")

if __name__ == "__main__":
    create_submission()