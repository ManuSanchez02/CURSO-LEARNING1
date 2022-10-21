from re import sub

class SimplePigLatin:
    # Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
    # Examples
    #
    # pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    # pig_it('Hello world !')     # elloHay orldway !
    def pig_it(text):
        return " ".join([word[1:] + word[0] + "ay" if word not in ["!", "?"] else word for word in (text.split())])

class TheHashtagGenerator:
    # The marketing team is spending way too much time typing in hashtags.
    # Let's help them with our own Hashtag Generator!
    #
    # Here's the deal:
    #
    #     It must start with a hashtag (#).
    #     All words must have their first letter capitalized.
    #     If the final result is longer than 140 chars it must return false.
    #     If the input or the result is an empty string it must return false.
    #
    # Examples
    #
    # " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
    # "    Hello     World   "                  =>  "#HelloWorld"
    # ""
    @staticmethod
    def generate_hashtag(s):
        res = "#" + s.title()
        res = res.replace(" ", "")
        largo = len(res)
        if largo == 1 or largo > 140:
            return False
        return res

class MovingZerosToTheEnd:
    # Write an algorithm that takes an array and moves all of the zeros to the end,
    # preserving the order of the other elements.
    #
    # move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

    def move_zeros(lst):
        return sorted(lst, key=lambda x: x == 0)


class ValidParentheses:
    # Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
    # The function should return true if the string is valid, and false if it's invalid.
    # Examples
    #
    # "()"              =>  true
    # ")(()))"          =>  false
    # "("               =>  false
    # "(())((()())())"  =>  true
    #
    # Constraints
    #
    # 0 <= input.length <= 100
    #
    # Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore,
    # the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets
    # as parentheses (e.g. [], {}, <>).

    @staticmethod
    def valid_parentheses(string):
        # your code here
        c = []
        try:
            [c.append(None) if x == "(" else c.pop() for x in string if x in "()"]
        except:
            return False
        return len(c) == 0
