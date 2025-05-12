
import os

for dirpath, dirnames, filenames in os.walk("MOD 5"):
    print("Current Directory:", dirpath)
    print("Subdirectories:", dirnames)
    print("Files:", filenames)
