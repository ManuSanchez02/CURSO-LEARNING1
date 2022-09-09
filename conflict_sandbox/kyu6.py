from string import ascii_lowercase
from collections import Counter

class DetectPangram:
    # A pangram is a sentence that contains every single letter of the alphabet at least once.
    # For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
    # because it uses the letters A-Z at least once (case is irrelevant).
    # Given a string, detect whether or not it is a pangram.
    # Return True if it is, False if not. Ignore numbers and punctuation.

    @staticmethod
    def is_pangram(s):
        letter_list = [ch for ch in sorted(set(list(s.lower()))) if ch in ascii_lowercase]
        return letter_list == list(ascii_lowercase)


class TakeATenMinutesWalk:
    # You live in the city of Cartesia where all roads are laid out in a perfect grid.
    # You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
    # The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it
    # sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
    # You know it takes you one minute to traverse one city block, so create a function that will return true if the
    # walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course,
    # return you to your starting point. Return false otherwise.
    #
    # Note: you will always receive a valid array containing a random assortment of direction letters.
    # It will never give you an empty array (that's not a walk, that's standing still!).

    @staticmethod
    def isValidWalk(walk):
        if len(walk) != 10:
            return False
        if walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e'):
            return True
        else:
            return False

class YourOrderPlease:
    # Your task is to sort a given string. Each word in the string will contain a single number.
    # This number is the position the word should have in the result.
    #
    # Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
    #
    # If the input string is empty, return an empty string. The words in the input String will only contain
    # valid consecutive numbers.
    #
    # Examples
    #
    # "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
    # "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
    # ""  -->  ""

    @staticmethod
    def order(sentence):
        return " ".join(sorted(sentence.split(), key=lambda w: [int(c) for c in w if c.isdigit()][0]))

class DuplicateEncoder:
    # The goal of this exercise is to convert a string to a new string where each character in the new string is
    # "(" if that character appears only once in the original string, or ")" if that character appears more than once
    # in the original string. Ignore capitalization when determining if a character is a duplicate.
    #
    # Examples
    #
    # "din"      =>  "((("
    # "recede"   =>  "()()()"
    # "Success"  =>  ")())())"
    # "(( @"     =>  "))(("
    #
    # Notes
    #
    # Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

    duplicate_encode = lambda word: "".join(["(" if word.lower().count(x.lower()) == 1 else ")" for x in word])

    @staticmethod
    def duplicate_encode(word):
        encoded = ''
        for character in word.lower():
            if word.lower().count(character) == 1:
                encoded += '('
            else:
                encoded += ')'
        return encoded
