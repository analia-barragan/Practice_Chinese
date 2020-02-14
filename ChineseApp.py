import argparse
from Functions_AddVocab import *


parser = argparse.ArgumentParser(description = 'Add new vocabulary', add_help =
True)

parser.add_argument('file_path', action = 'store', help = 'This is the file\
path to the dictionary with all the vocabulary', type = str)

args = parser.parse_args()

vocabulary = open_json(args.file_path)

actions = ['Add new vocabulary to a file', 'Correct an entry in the file',
'Test my vocabulary', 'I\'m done and want to exit the program']
option = pick_action()

while option != actions[3]:
    if option == actions[0]:
        add_vocabulary_multiple(vocabulary)
        save_file(args.file_path, vocabulary)
        print('Thank you for adding new vocabulary')
    if option == actions[1]:
        correct_entry(vocabulary, ['character', 'meaning', 'tone', 'pinyin'])
    if option == actions[2]:
        print('This is in development')
#is it possible to lag this a bit?
    option = pick_action()
#renshi and q to correct
