This script is used to clear duplicates images within the same subdirectory.

          example: python duplicatesRemoval.py 'databaseDirectory'

the script will walk through the provided directory and will access each subdirectory (category) and check for duplicates images using Perceptual Hashing.

The output is written in the root folder with `duplicateslog-YYYYMMDD-HHMMSS.txt` 
Contains the dictionary with possible duplicates with one of the image removed from the directory.