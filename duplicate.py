# For hashing the image data for detecting duplicate images
import hashlib
import os
from os import path
def remove_duplicates(path):
    files = os.listdir(path)
    os.chdir(path)
    duplicates = []
    hash_keys = dict()
    for index, filename in enumerate(os.listdir('.')):
        if os.path.isfile(filename):
            with open(filename,'rb') as f:
                filehash = hashlib.md5(f.read()).hexdigest()
            if filehash not in hash_keys:
                hash_keys[filehash] = index
            else:
                duplicates.append((index,hash_keys[filehash]))
    for index in duplicates:
        os.remove(files[index[0]])
