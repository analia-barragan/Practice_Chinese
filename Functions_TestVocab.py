import random
import numpy as np
def user_promt_test_legth():
    '''This function asks the user to define a test length
    INPUT: None
    OUTPUT: Test length provided by the user
    '''
    start = input('Are you ready to start Y/N? ')
    if start.lower() == 'y':
        test_length = int(input('How long should your test be? '))
    return test_length

def user_prompt_test_knowledge(dict_key, character):
    ''' This function returns the user's answer to a knowledge question.
    INPUT: Dictionary key e.g. "meaning" or "tone"
    OUTPUT: User answer
    '''
    return input('What is the {} of {} '.format(dict_key, character))

def random_character(vocab_dict):
    '''This function has the goal of randomly selecting a character from a dictionary
    INPUT: Dictionary with vocabulary
    OUTPU: Index of randomly selected character, character
    '''
    index = random.randint(0, (len(vocab_dict)-1))
    character = vocab_dict[index]['character']
    return index, character

def points(points):
    '''This function checks if the user answered the test correctly
    INPUT: Number of points
    OUTPUT: Boolean, True if a point was achieved, False if no point was achieved'''
    result = False
    if points == 3:
        result = True
    return result

def test_knowledge_one_character(vocab_dict, keys_list , index, character):
    '''This function tests the knowledge of the user for one single charatcer
    INPUT: Dictionary containing vocabulary, list of keys in dictionary (e.g meaning, tone),
    index in dictionary of character that should be tested, character that should be tested
    OUTPUT: Boolean, True if a point was achieved, False if no point was achieved'''
    keys = keys_list
    correct = 0
    for k in keys:
        user_input = user_prompt_test_knowledge(k, character)
        if vocab_dict[index][k] == user_input:
            print('Good job!')
            correct += 1
        else:
            print('Ups, that is not correct')
            print('The correct answer is: {}'.format(vocab_dict[index][k]))
    return points(correct)

def test_knowledge_complete(vocab_dict, keys_list):
    '''This function tests the knowledge of the user for the provided test_lenght.
    INPUT: Dictionary containing vocabulary, list of keys in dictionary (e.g meaning, tone)
    OUTPUT: None'''
    test_length = user_promt_test_legth()
    tested_characters = []
    score = 0
    for i in range(test_length):
        index, character = random_character(vocab_dict)
        while index in tested_characters:
            print('entered while loop')
            index, character = random_character(vocab_dict)

        if index not in tested_characters:
            tested_characters.append(index)
            points = test_knowledge_one_character(vocab_dict, keys_list, index, character)
            if points:
                score +=1
    print('You finished you test!')
    print('Your score is: {}/{} or {:.1f}%'.format(score, test_length, (score/test_length*100)))
