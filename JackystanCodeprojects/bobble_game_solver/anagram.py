"""
File: anagram.py
Name: Jacky Chang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This function search anagrams of user type in dictionary.txt
    """
    ####################
    print('Welcome to stanCode \"Anagram Generator\" (or ' + EXIT + ' to quit)')
    while True:
        s = input('Find anagrams for: ')
        start = time.time()
        if s == EXIT:
            break
        find_anagrams(s)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')
    ####################


def read_dictionary(s):
    word_lst = []
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) == len(s) and word[0] in s:
                word_lst.append(word)
    return word_lst


# def matching_ch(s, word):
#     for alpha in word:
#         if alpha not in s:
#             return False
#     return True


def find_anagrams(s):
    """
    :param s: str, user type to search anagrams
    :return: print a list, contain all anagrams and count the number of anagrams
    """
    word_lst = read_dictionary(s)
    answer_lst = []
    find_anagrams_helper(s, '', len(s), answer_lst, [], word_lst)
    print('Searching...')
    print(str(len(answer_lst)), ' anagrams: ', answer_lst)


def find_anagrams_helper(s, current_s, ans_len, answer_lst, index_lst, word_lst):
    """
    :param s: str, user type to search anagrams
    :param current_s: str, empty str for anagram searching
    :param ans_len: int, len of str that user type to search anagrams
    :param answer_lst: list, to save answer anagrams
    :param index_lst: list, to save index for anagram searching
    :param word_lst: list, consistent with all words in dictionary
    :return: list, contain all anagrams and count the number of anagrams
    """
    if len(current_s) == ans_len:
        if current_s in word_lst:
            if current_s not in answer_lst:
                print('Searching...')
                print('Found: ' + current_s)
                answer_lst.append(current_s)
    else:
        for i in range(len(s)):
            if i not in index_lst:
                # Choose
                current_s += s[i]
                index_lst.append(i)
                if has_prefix(current_s, word_lst):
                    # explore
                    find_anagrams_helper(s, current_s, ans_len, answer_lst, index_lst, word_lst)
                # Un_choose
                current_s = current_s[0:len(current_s)-1]
                index_lst.pop()


def has_prefix(sub_s, word_lst):
    """
    :param sub_s: str, consistent with any alphabet combinations from 's' user type
    :param word_lst: list, consistent with all words in dictionary
    :return: boolean, check if word in word_lst start with sub_s
    """
    for word in word_lst:
        if word.startswith(sub_s):
            return True
    return False

    # a, aa, aaron, .... , zulu


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)


if __name__ == '__main__':
    main()
