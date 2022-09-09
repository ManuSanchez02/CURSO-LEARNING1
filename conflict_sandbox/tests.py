import unittest
import TestRunner
from kyu5 import SimplePigLatin, TheHashtagGenerator, MovingZerosToTheEnd, ValidParentheses
from kyu7 import FriendOrFoe, RegexValidatePinCode, HighestAndLowest, VowelCount
from kyu6 import DetectPangram, TakeATenMinutesWalk, YourOrderPlease, DuplicateEncoder

from random import choice, randint, shuffle, choices, sample
from string import ascii_letters as abc
from itertools import product, permutations


class FriendOrFoeTests(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(["Ryan", "Mark"], FriendOrFoe.friend(["Ryan", "Kieran", "Mark", ]))
        self.assertEqual(["Ryan"], FriendOrFoe.friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]))
        self.assertEqual(["Jimm", "Cari", "aret"],
                         FriendOrFoe.friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))
        self.assertEqual(["Love", "Your", "Face"], FriendOrFoe.friend(["Love", "Your", "Face", "1"]))
        self.assertEqual(["Hell", "badd", "word"], FriendOrFoe.friend(["Hell", "Is", "a", "badd", "word"]))
        self.assertEqual(["Issa"], FriendOrFoe.friend(["Issa", "Issac", "Issacs", "ISISS"]))
        self.assertEqual(["Your"], FriendOrFoe.friend(["Robot", "Your", "MOMOMOMO"]))
        self.assertEqual(["Your", "BUTT"], FriendOrFoe.friend(["Your", "BUTT"]))
        self.assertEqual(["Gupt"], FriendOrFoe.friend(["Hello", "I", "AM", "Sanjay", "Gupt"]))
        self.assertEqual(["This", "TEst", "CaSe"], FriendOrFoe.friend(["This", "IS", "enough", "TEst", "CaSe"]))
        self.assertEqual([], FriendOrFoe.friend([]))

    def random_string(self,friend=False):
        return "".join(choice(abc) for _ in range(friend and 4 or randint(0, 20)))

    def random_input(self):
        return [self.random_string(randint(0, 100) % 4 == 0) for _ in range(randint(0, 20))]

    def solution(self,l):
        return [w for w in l if len(w) == 4]

    def test_random_cases(self):
        for _ in range(100):
            ri = self.random_input()
            expected = self.solution(ri)
            self.assertListEqual(FriendOrFoe.friend(ri), expected)


class RegexValidatePinCodeTests(unittest.TestCase):
            
    def test_false_for_invalid_length(self):
            # should return False for pins with length other than 4 or 6
            self.assertEqual(False, RegexValidatePinCode.validate_pin("1"), "Wrong output for '1'")
            self.assertEqual(False, RegexValidatePinCode.validate_pin("12"), "Wrong output for '12'")
            self.assertEqual(False, RegexValidatePinCode.validate_pin("123"), "Wrong output for '123'")
            self.assertEqual(False, RegexValidatePinCode.validate_pin("12345"), "Wrong output for '12345'")
            self.assertEqual(False, RegexValidatePinCode.validate_pin("1234567"), "Wrong output for '1234567'")
            self.assertEqual(False, RegexValidatePinCode.validate_pin("-1234"), "Wrong output for '-1234'")
            self.assertEqual(False, RegexValidatePinCode.validate_pin("-12345"), "Wrong output for '-12345'")
            self.assertEqual(False, RegexValidatePinCode.validate_pin("1.234"), "Wrong output for '1.234'")
            self.assertEqual(False, RegexValidatePinCode.validate_pin("00000000"), "Wrong output for '00000000'")

    def test_false_for_invalid_characters(self):
            self.assertEqual(False, RegexValidatePinCode.validate_pin("a234"), "Wrong output for 'a234'")
            self.assertEqual(False, RegexValidatePinCode.validate_pin(".234"), "Wrong output for '.234'")

    def test_valid_inputs(self):
        self.assertEqual(True, RegexValidatePinCode.validate_pin("1234"), "Wrong output for '1234'")
        self.assertEqual(True, RegexValidatePinCode.validate_pin("0000"), "Wrong output for '0000'")
        self.assertEqual(True, RegexValidatePinCode.validate_pin("1111"), "Wrong output for '1111'")
        self.assertEqual(True, RegexValidatePinCode.validate_pin("123456"), "Wrong output for '123456'")
        self.assertEqual(True, RegexValidatePinCode.validate_pin("098765"), "Wrong output for '098765'")
        self.assertEqual(True, RegexValidatePinCode.validate_pin("000000"), "Wrong output for '000000'")
        self.assertEqual(True, RegexValidatePinCode.validate_pin("123456"), "Wrong output for '123456'")
        self.assertEqual(True, RegexValidatePinCode.validate_pin("090909"), "Wrong output for '090909'")

class HighestAndLowestTests(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual("542 -214", HighestAndLowest.high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"));
        self.assertEqual("1 -1", HighestAndLowest.high_and_low("1 -1"));
        self.assertEqual("1 1", HighestAndLowest.high_and_low("1 1"));
        self.assertEqual("-1 -1", HighestAndLowest.high_and_low("-1 -1"));
        self.assertEqual("1 -1", HighestAndLowest.high_and_low("1 -1 0"));
        self.assertEqual("1 0", HighestAndLowest.high_and_low("1 1 0"));
        self.assertEqual("0 -1", HighestAndLowest.high_and_low("-1 -1 0"));
        self.assertEqual("42 42", HighestAndLowest.high_and_low("42"));

    def test_random_cases(self):
        for t in range(10):
            lo = randint(-500, 500)
            hi = lo + 3000 + randint(1, 100)
            arg = [hi, lo] + [str(lo + randint(1, 2999)) for i in range(20)]
            shuffle(arg)
            arg = " ".join(str(a) for a in arg)
            exp = "%i %i" % (hi, lo)

            self.assertEqual(exp, HighestAndLowest.high_and_low(arg))


class DetectPanagramTests(unittest.TestCase):

    def test_pangram(self):
        self.assertEqual(True, DetectPangram.is_pangram("The quick, brown fox jumps over the lazy dog!"))

    def test_not_pangram(self):
        self.assertEqual(False, DetectPangram.is_pangram("1bcdefghijklmnopqrstuvwxyz"))

    def test_fixed_pangrams(self):
        pangrams = ["The quick brown fox jumps over the lazy dog.",
                    "Cwm fjord bank glyphs vext quiz",
                    "Pack my box with five dozen liquor jugs.",
                    "How quickly daft jumping zebras vex.",
                    "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"]
        for pangram in pangrams:
            self.assertEqual(True, DetectPangram.is_pangram(pangram), f"Incorrect answer for '{pangram}'")

    def test_fixed_non_pangrams(self):
        non_pangrams = ["This isn't a pangram!",
                        "abcdefghijklm opqrstuvwxyz",
                        "Aacdefghijklmnopqrstuvwxyz"]
        for non_pangram in non_pangrams:
            self.assertEqual(False, DetectPangram.is_pangram(non_pangram), f"Incorrect answer for '{non_pangram}'")


class VowelCountTests(unittest.TestCase):

    vowels = "aeiou"
    nonvowels = "bcdfghjklmnpqrstvwxyz"

    def test_all_vowels(self):
        self.assertEqual(5, VowelCount.getCount("aeiou"), f"Incorrect answer for \"aeiou\"")

    def test_only_y(self):
        self.assertEqual(0, VowelCount.getCount("y"), f"Incorrect answer for \"y\"")

    def test_no_vowels(self):
        self.assertEqual(0, VowelCount.getCount("bcdfghjklmnpqrstvwxz y"),
                         f"Incorrect answer for \"bcdfghjklmnpqrstvwxz y\"")

    def test_string_empty(self):
        self.assertEqual(0, VowelCount.getCount(""), f"Incorrect answer for empty string")

    def test_abracadabra(self):
        self.assertEqual(5, VowelCount.getCount("abracadabra"), f"Incorrect answer for \"abracadabra\"")
    
    def generate_tests(self, generator, count):
        return [generator() for _ in range(count)]

    def generate_no_vowels(self):
        word_count = randint(1, 10)
        words = ["".join(choices(self.nonvowels, k=randint(1, 8))) for _ in range(word_count)]
        sentence = " ".join(words)
        return (sentence, 0)

    def generate_only_vowels(self):
        word_count = randint(1, 10)
        words = ["".join(choices(self.vowels, k=randint(1, 8))) for _ in range(word_count)]
        sentence = " ".join(words)
        return (sentence, sum(len(word) for word in words))

    def generate_mixed(self):
        word_count = randint(1, 10)
        vowel_parts = ["".join(choices(self.vowels, k=randint(1, 3))) for _ in range(word_count)]
        nonvowel_parts = ["".join(choices(self.nonvowels, k=randint(1, 8))) for _ in range(word_count)]
        words = ["".join(sample(v + nv, k=len(v + nv))) for v, nv in zip(vowel_parts, nonvowel_parts)]
        sentence = " ".join(words)
        return (sentence, sum(len(word) for word in vowel_parts))
    
    def test_random(self):
        test_cases = self.generate_tests(self.generate_no_vowels, 10) + \
                     self.generate_tests(self.generate_only_vowels, 10) + \
                     self.generate_tests(self.generate_mixed, 80)
        shuffle(test_cases)

        for input, expected in test_cases:
            actual = VowelCount.getCount(input)
            self.assertEqual(expected, actual,
                             f"Incorrect answer for input: \"{input}\"\nActual: {actual}\nExpected: {expected}")


class TakeATenMinutesWalkTests(unittest.TestCase):
    def isValidWalkforthisscope(self, walk):
        pos = [0, 0]
        for i in range(len(walk)):
            if walk[i] == 'n':
                pos[0] += 1
            if walk[i] == 's':
                pos[0] -= 1
            if walk[i] == 'w':
                pos[1] += 1
            if walk[i] == 'e':
                pos[1] -= 1
        if pos == [0, 0] and len(walk) == 10:
            return True
        return False

    def create_tests(self, length):
        poss = ['n', 'w', 'e', 's']
        res = [choice(poss) for _ in range(length)]
        x = self.isValidWalkforthisscope(res)
        return [res, x]

    def test_valid_wak(self):
        self.assertEqual(True, TakeATenMinutesWalk.isValidWalk("wnnwwsseee"))

    def test_more_than_ten_minutes(self):
        self.assertEqual(False, TakeATenMinutesWalk.isValidWalk("wwnnwwsseeee"))

    def test_less_than_ten_minutes(self):
        self.assertEqual(TakeATenMinutesWalk.isValidWalk("nsew"), False)

    def test_empty(self):
        self.assertEqual(False, TakeATenMinutesWalk.isValidWalk(""))

    def test_doesnt_return_home(self):
        self.assertEqual(TakeATenMinutesWalk.isValidWalk("nnwweennss"), False)

    def test_random_walks(self):
        for _ in range(100):
            test1 = self.create_tests(randint(0, 20))
            self.assertEqual(test1[1], TakeATenMinutesWalk.isValidWalk(test1[0]))


class YourOrderPleaseTests(unittest.TestCase):
    def test_static(self):
        self.assertEqual("Fo1r the2 g3ood 4of th5e pe6ople", YourOrderPlease.order("4of Fo1r pe6ople g3ood th5e the2"))
        self.assertEqual("wha1t sh2all 3we d4o w5ith a6 dru7nken s8ailor",
                         YourOrderPlease.order("d4o dru7nken sh2all w5ith s8ailor wha1t 3we a6"))
        self.assertEqual("", YourOrderPlease.order(""))
        self.assertEqual("1 2 3 4 5 6 7 8 9", YourOrderPlease.order("3 6 4 2 8 7 5 1 9"))

    def test_random(self):
        WORDS = "a able about after all an and as ask at bad be big but by call case child come company day different do early eye fact feel few find first for from get give go good government great group hand have he her high his I important in into it know large last leave life little long look make man my new next not number of old on one or other over own part person place point problem public right same say see seem she small take tell that the their there they thing think this time to try up use want way week will with woman work work world would year you young".split()

        for _ in range(50):
            arr = sample(WORDS, randint(0, 9))
            arr2 = []
            for i, w in enumerate(arr):
                letters = list(w)
                letters.insert(randint(0, len(w)), str(i + 1))
                arr2.append("".join(letters))
            expected = " ".join(arr2)
            shuffle(arr2)
            test_str = " ".join(arr2)

            self.assertEqual(expected, YourOrderPlease.order(test_str))

class DuplicateEncoderTests(unittest.TestCase):
    def test_sample_cases(self):
        self.assertEqual("(((", DuplicateEncoder.duplicate_encode("din"))
        self.assertEqual("()()()", DuplicateEncoder.duplicate_encode("recede"))
        self.assertEqual(")())())", DuplicateEncoder.duplicate_encode("Success"), "should ignore case")
        self.assertEqual("))((", DuplicateEncoder.duplicate_encode("(( @"))
        self.assertEqual("()(((())())", DuplicateEncoder.duplicate_encode("CodeWarrior"))
        self.assertEqual(")()))()))))()(", DuplicateEncoder.duplicate_encode("Supralapsarian"), "should ignore case")
        self.assertEqual("))))))", DuplicateEncoder.duplicate_encode("iiiiii"), "duplicate-only-string")

    def test_with_parentheses(self):
        self.assertEqual("))((", DuplicateEncoder.duplicate_encode("(( @"))
        self.assertEqual(")))))(", DuplicateEncoder.duplicate_encode(" ( ( )"))

    def test_random_cases(self):
        duplicate_sol = lambda word: "".join(["(" if word.lower().count(x.lower())==1 else ")" for x in word])
        for _ in range(40):
            testlen=randint(6,40)
            testword=""
            for i in range(testlen):
                testword+="abcdeFGHIJklmnOPQRSTuvwxyz() @!"[randint(0,30)]
            self.assertEqual(duplicate_sol(testword), DuplicateEncoder.duplicate_encode(testword),
                             "It Should encode '" + duplicate_sol(testword) + "'")


class SimplePigLatinTests(unittest.TestCase):
    def test_sample_cases(self):
        self.assertEqual('igPay atinlay siay oolcay', SimplePigLatin.pig_it('Pig latin is cool'))
        self.assertEqual('hisTay siay ymay tringsay', SimplePigLatin.pig_it('This is my string'))

    def test_random_cases(self):
        base = [
            ['Acta est fabula', 'ctaAay steay abulafay'],
            ['Barba non facit philosophum', 'arbaBay onnay acitfay hilosophumpay'],
            ['Cucullus non facit monachum', 'ucullusCay onnay acitfay onachummay'],
            ['Dura lex sed lex', 'uraDay exlay edsay exlay'],
            ['Errare humanum est', 'rrareEay umanumhay steay'],
            ['Fluctuat nec mergitur', 'luctuatFay ecnay ergiturmay'],
            ['Gutta cavat lapidem', 'uttaGay avatcay apidemlay'],
            ['Hic et nunc', 'icHay teay uncnay'],
            ['In vino veritas', 'nIay inovay eritasvay'],
            ['Lux in tenebris lucet', 'uxLay niay enebristay ucetlay'],
            ['Morituri nolumus mori', 'orituriMay olumusnay orimay'],
            ['Nunc est bibendum', 'uncNay steay ibendumbay'],
            ['O tempora o mores !', 'Oay emporatay oay oresmay !'],
            ['Panem et circenses', 'anemPay teay ircensescay'],
            ['Quis custodiet ipsos custodes ?', 'uisQay ustodietcay psosiay ustodescay ?'],
            ['Requiescat in pace', 'equiescatRay niay acepay'],
            ['Sic transit gloria mundi', 'icSay ransittay loriagay undimay'],
            ['Timeo Danaos et dona ferentes', 'imeoTay anaosDay teay onaday erentesfay'],
            ['Ultima necat', 'ltimaUay ecatnay'],
            ['Veni vidi vici', 'eniVay idivay icivay']]
        shuffle(base)
        for item in base:
            self.assertEqual(item[1], SimplePigLatin.pig_it(item[0]), "You should 'pig' \"" + item[1] + "\"")


class TheHashtagGeneratorTests(unittest.TestCase):

    def test_sample_cases(self):        
        self.assertEqual(False, TheHashtagGenerator.generate_hashtag(''), 'Expected an empty string to return False')
        self.assertEqual('#', TheHashtagGenerator.generate_hashtag('Do We have A Hashtag')[0],
                         'Expeted a Hashtag (#) at the beginning.')
        self.assertEqual('#Codewars', TheHashtagGenerator.generate_hashtag('Codewars'), 'Should handle a single word.')
        self.assertEqual('#Codewars', TheHashtagGenerator.generate_hashtag('Codewars      '),
                         'Should handle trailing whitespace.')
        self.assertEqual('#CodewarsIsNice', TheHashtagGenerator.generate_hashtag('Codewars Is Nice'),
                         'Should remove spaces.')
        self.assertEqual('#CodewarsIsNice', TheHashtagGenerator.generate_hashtag('codewars is nice'),
                         'Should capitalize first letters of words.')
        self.assertEqual('#CodewarsIsNice', TheHashtagGenerator.generate_hashtag('CodeWars is nice'),
                         'Should capitalize all letters of words - all lower case but the first.')
        self.assertEqual('#CIN', TheHashtagGenerator.generate_hashtag('c i n'),
                         'Should capitalize first letters of words even when single letters.')
        self.assertEqual('#CodewarsIsNice', TheHashtagGenerator.generate_hashtag('codewars  is  nice'),
                         'Should deal with unnecessary middle spaces.')
        self.assertEqual(False, TheHashtagGenerator.generate_hashtag(
            'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'),
                         'Should return False if the final word is longer than 140 chars.')
        self.assertEqual("#HelloWorld!", TheHashtagGenerator.generate_hashtag(
            '                                                  Hello                                                  world!                                                  '),
                         'The length of the input string may be longer than 140 characters.')

    def test_random_cases(self):
        sol = lambda s: (lambda s: False if len(s) == 1 or len(s) > 140 else s)("#" + "".join(
            "" if l == " " else l.upper() if i == 0 or s[i - 1] == " " else l.lower() for i, l in enumerate(s)))
        base = "abcdefghijklmnopqrstuvwxyz  ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # Changed from 40 to 35 to keep the overall number of tests the same
        for _ in range(35):
            s = " ".join(["".join(base[randint(0, len(base) - 1)] for q in range(1, 12)) for x in range(randint(1, 8))])
            self.assertEqual(sol(s), TheHashtagGenerator.generate_hashtag(s), "It should work for random inputs too")

        # Generate some heavily spaced out tests to make sure solutions correctly handle cases where
        # input length is > 140 but output length is < 140
        for _ in range(5):
            s = (" " * 30).join(
                ["".join(base[randint(0, len(base) - 1)] for q in range(1, 12)) for x in range(randint(4, 8))])
            self.assertEqual(sol(s), TheHashtagGenerator.generate_hashtag(s), "It should work for random inputs too")


class MovingZerosToTheEndTests(unittest.TestCase):

    def test_sample_cases(self):
        self.assertEqual([1, 2, 1, 1, 3, 1, 0, 0, 0, 0], MovingZerosToTheEnd.move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
        self.assertEqual([9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], MovingZerosToTheEnd.move_zeros(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
        self.assertEqual([0, 0], MovingZerosToTheEnd.move_zeros([0, 0]))
        self.assertEqual([0], MovingZerosToTheEnd.move_zeros([0]))
        self.assertEqual([], MovingZerosToTheEnd.move_zeros([]))


    def fixed(self):
        # Attempt to cover all corner cases by generating all possibilities of
        # size 0,1,2,3,4 lists with 0,1,2 elements.
        # This produces 121 cases.
        for size in range(5):
            yield from map(list, product([0, 1, 2], repeat=size))


    def cases_without_zeros(self):
        sizes = list(range(10)) * 2
        for size in sizes:
            yield list(choices(range(1, 10), k=size))


    def cases_with_zeros(self):
        zeros = range(5, 10)
        nonzs = range(5)
        for zero, nonzero in product(zeros, nonzs):
            xs = choices(range(1, 10), k=nonzero) + ([0] * zero)
            shuffle(xs)
            yield xs

    def test_random_cases(self):
        cases = [*self.cases_with_zeros(), *self.cases_without_zeros(), *self.fixed()]
        shuffle(cases)
        for xs in cases:
            expected = [x for x in xs if x != 0] + [x for x in xs if x == 0]
            self.assertEqual(expected, MovingZerosToTheEnd.move_zeros(xs))


class ValidParenthesesTest(unittest.TestCase):

    def test_sample_cases(self):
        self.assertEqual(False, ValidParentheses.valid_parentheses("  ("), "should work for '  ('")
        self.assertEqual(False, ValidParentheses.valid_parentheses(")test"), "should work for ')test'")
        self.assertEqual(True, ValidParentheses.valid_parentheses(""), "should work for ''")
        self.assertEqual(False, ValidParentheses.valid_parentheses("hi())("), "should work for 'hi())('")
        self.assertEqual(True, ValidParentheses.valid_parentheses("hi(hi)()"), "should work for 'hi(hi)()'")

    def act(self, parens, expected):
        self.assertEqual(expected, ValidParentheses.valid_parentheses(parens))

    def test_fixed_cases(self):
        self.act(")", False)
        self.act("(", False)
        self.act("", True)
        self.act("hi)(", False)
        self.act("hi(hi)", True)
        self.act("(", False)
        self.act("hi(hi)(", False)
        self.act("((())()())", True)
        self.act("(c(b(a)))(d)", True)
        self.act("hi(hi))(", False)
        self.act("())(()", False)

    def test_random_cases(self):
        base = "abcdefghijklmnopqrstuvwxyz()"
        isSol = lambda string: all(
            [string[:i].count(")") <= string[:i].count("(") for i in range(len(string) + 1)]) and string.count(
            "(") == string.count(")")
        for _ in range(40):
            testlen = randint(5, 40)
            teststring = ["()", "()()", "(())", "()(())()"][randint(0, 3)]
            for i in range(testlen):
                pos = randint(0, len(teststring))
                teststring = teststring[:pos] + base[randint(0, len(base) - 1)] + teststring[pos:]
            self.act(teststring, isSol(teststring))

if __name__ == '__main__':
    unittest.main(testRunner = TestRunner.TestRunner())