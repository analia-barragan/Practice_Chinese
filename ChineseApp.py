import argparse
from Functions_AddVocab import *

parser = argparse.ArgumentParser(description = 'Add new vocabulary', add_help =
True)

parser.add_argument('file_path', action = 'store', help = 'This is the file\
path to the dictionary with all the vocabulary', type = str)

args = parser.parse_args()
