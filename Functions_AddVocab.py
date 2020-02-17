from pick import pick
import json

def pick_action():
    title = ' What would you like to do?'
    options = ['Add new vocabulary to a file', 'Correct an entry in the file',
    'Test my vocabulary', 'I\'m done and want to exit the program']
    option, index = pick(options, title)
    return option


def open_json(file_path):
    '''This function opens a JSON file.
    INPUT: File path to JSON
    OUTPUT: Readable file
    '''
    with open(file_path, 'r') as file:
        vocabulary = json.load(file)
        return vocabulary

def check_if_in_dictionary(character, vocab_dict):
    '''This function checks if a specific character already exists in the dictionary.
    INPUT: Specific character, dictionary containing vocabulary
    OUTPUT: Boolean, True is character is in dictionary, False if character is not in dictionary,
    index of character in list
    '''
    is_there = False
    index = None
    for i in range(len(vocab_dict)):
        if character == vocab_dict[i]['character']:
            is_there = True
            index = i
    return is_there, index

def user_prompt(vocab_dict):
    '''This function contains user promts to gather vocabulary input.
    INPUT: Dictionary containing vocabulary
    OUTPUT: User input for character, meaning in english, tone, pinyin'''
    character_i = input('Please type in the Chinese character: ')
    is_there, index = check_if_in_dictionary(character_i, vocab_dict)
    while is_there:
        print('This character is already in the dictionary')
        character_i = input('Please type a new Chinese character: ')
        is_there, index = check_if_in_dictionary(character_i, vocab_dict)
    meaning_i = input('Please type the english meaning of this chinese character: ')
    tone_i = (input('Please provide the tone of this chinese character(s) (1-4): '))
    pinyin_i = input('Please provide the pinyin of this chinese character: ')
    return character_i, meaning_i, tone_i, pinyin_i

def add_vocabulary_simple(vocab_dict):
    '''This function appends a single data entry to the dictionary containing the vocabulary
    INPUT: Dictionary containing the vocabulary
    OUTPUT: None'''
    character_i, meaning_i,tone_i, pinyin_i = user_prompt(vocab_dict)
    vocab_dict.append({'character': character_i, 'meaning': meaning_i,
                       'tone': tone_i, 'pinyin': pinyin_i})
    print('\nFollowing values have been added to the vocabulary:\nCharacter: {}\nMeaning: {}\nTone: {}\nPinyin: {}'.format(character_i,meaning_i,
                                                                   tone_i, pinyin_i))

def add_vocabulary_multiple(vocab_dict):
    '''This function appends multiple single data entry to the dictionary containing the vocabulary
    INPUT: Dictionary containing the vocabulary
    OUTPUT: None'''
    add_vocabulary_simple(vocab_dict)
    continue_asking = input('\nDo you want to add more characters? Enter Y/N: ')
    while continue_asking.lower() == 'y':
        add_vocabulary_simple(vocab_dict)
        continue_asking = input('\nDo you want to add more characters? Enter Y/N: ')


def user_promt_correct(vocab_dict, options):
    character = input('What character do you want to correct?')
    is_there, index = check_if_in_dictionary(character, vocab_dict)
    user_feedback = vocab_dict[index].copy()
    answers = {}
    if not is_there:
        print('This character in not in the dictionary')
    else:
        for opt in options:
            user_i = input('This is the {} at the moment: {}\nDo you want to correct the {}?(Y/N)'.format(opt, user_feedback[opt], opt))
            if user_i.lower() == 'y':
                answers[opt]= input('Please input the corrected {}: '.format(opt))
    return answers, user_feedback, index

def correct_entry(vocab_dict, dict_options):
    answers, original, index = user_promt_correct(vocab_dict, dict_options)
    for a in answers:
        vocab_dict[index][a] = answers[a]
    print('The entry\n{}\nhas been replaced by\n{}'.format(original, vocab_dict[index]))

def save_file(file_path, vocab_dict):
    '''This function saves dictionary containing vocabulary to a JSON
    INPUT: Dictionary containing vocabulary
    OUTPUT: None'''
    with open(file_path, 'w') as outfile:
        json.dump(vocab_dict, outfile)
