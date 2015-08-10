import re
import functools
import random
import itertools
import collections
from collections import defaultdict


# 3. str_len()s
def str_len(s):
    i = 0
    for char in s:
        i += 1
    return i


# 4. is_vowel()
def is_vowel(c):
    vowels = ('aeiou')
    if len(c) == 1:
        return c in vowels
    raise Exception('multiple characters in input')


# 5. translate()
def translate(original):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    translated = ''
    for letter in original:
        if not letter in consonants:
            translated += letter
        else:
            translated = translated + letter + 'o' + letter.lower()
    return translated


# 6. sum()
def sum(nums):
    result = 0
    for number in nums:
        result += number
    return result


# 6. multiply()
def multiply(nums):
    result = 1
    for number in nums:
        result *= number
    return result


# 7. reverse()
def reverse(string):
    result = ''
    index = 1
    for letter in string:
        result += string[str_len(string) - index]
        index += 1

    return result


# 8. is_palindrome()
def is_palindrome(string):
    return string == reverse(string)


# 9. is_member()
def is_member(x, a):
    for value in a:
        if x == value:
            return True
    return False


# 10. overlapping
def overlapping(list1, list2):
    for e1 in list1:
        for e2 in list2:
            if e1 == e2:
                return True
    return False


# 11. generate_n_chars()
def generate_n_chars(num, char):
    result = ''
    for i in range(num):
        result += char
    return result


# 12. histogram()
def histogram(list):
    for i in list:
        result = ''
        for j in range(i):
            result += '*'
        print(result)


# 13. max_in_list()
def max_in_list(list):
    result = list[0]
    for num in list:
        if num > result:
            result = num
    return result


# 14. map_words()
def map_words(list1):
    result = []
    for string in list1:
        result.append(len(string))
    return result


# 15. longest_word()
def longest_word(list1):
    return max_in_list(map_words(list1))


# 16. filter_long_words()
def filter_long_words(words, length):
    result = []
    for word in words:
        if len(word) >= length:
            result.append(word)
    return result


# 17. is_palindrome_advanced()
def is_palindrome_advanced(string):
    string = re.sub('[^A-Za-z]', '', string)
    return is_palindrome(string.lower())


# 18. is_pangram()
def is_pangram(string):
    char_set = set()
    universal_chars = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z'}
    string = (re.sub('[^A-Za-z]', '', string)).lower()
    for letter in string:
        char_set.add(letter)
    return char_set == universal_chars


# 19. bottles_of_beer()
def bottles_of_beer():
    song = "{0} bottles of beer on the wall, {0} bottle{2} of beer. Take one down, pass it around, {1} bottle{3} of beer on the wall"
    # print(song)
    for i in range(99, 0, -1):
        #    print(i)
        print(song.format(i, i - 1, 's' if i != 1 else '', 's' if i - 1 != 1 else ''))
        # i=i-1
        #  print(song)


# 20. translate_words_alt()

def translate_words_alt(list_1):
    result = []
    translation_dict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "år"}
    for word in list_1:
        result.append(translation_dict[word])
    return result


# 21.char_freq()
def char_freq(string):
    universal_chars = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z'}
    string = string.lower()
    result = {}
    for char in universal_chars:
        c = string.count(char)
        if (c > 0):
            result[char] = c
    return result


# 22. rot_13_decrypt
def rot_13_decrypt(string):
    dic1 = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
            'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
            'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
            'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
            'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
            'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
            'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
    result = ''
    keys = dic1.keys()
    for char in string:
        if char in keys:
            result += dic1[char]
        else:
            result += char
    # print(result)
    # print(rot_13_decrypt(rot_13_decrypt('Hey mama')))
    return result


# 23. correct()
def correct(string):
    string = re.sub(' +', ' ', string)
    string = re.sub(r'\.([^ ])', r'. \1', string)
    return string


# 24. make_3d_form
def make_3d_form(word):
    if re.search('y$', word):
        return re.sub('y$', 'ies', word)
    elif re.search('(o|ch|x|z|(sh?))$', word):
        return re.sub('$', 'es', word)
    else:
        return re.sub('$', 's', word)


# 25. make_ing_form
def make_ing_form(word):
    if re.search('[^i]e$', word):
        return re.sub('e$', 'ing', word)
    elif re.search('ie$', word):
        return re.sub('ie$', 'ying', word)
    elif re.search('[^aieou][aieuo][^aieou]$', word):
        return re.sub('(.)$', r'\1\1ing', word)
    else:
        return re.sub('$', 'ing', word)


# 26. max_in_list_v1()
def max_in_list_v1(list1):
    def compare(x, y):
        if x > y:
            return x
        else:
            return y

    return functools.reduce(compare, list1)


# 27.map_words_v1
def map_words_v1(list_words):
    return [len(word) for word in list_words]


# 27.1 map_words_v2
def map_words_v2(list_words):
    return list(map_v1(len, list_words))


# 28. find_longest_word_advanced()
def find_longest_word_advanced(list_words):
    return max_in_list(map_words_v1(list_words))


# 29. filter_long_words_advanced()
def filter_long_words_advanced(list_1, n):
    return list(filter(lambda x: len(x) >= n, list_1))


# 31.1 map_v1()
def map_v1(func1, iterable1):
    return [func1(iter1) for iter1 in iterable1]


# 31.2 filter_v1()
def filter_v1(func1, iterable1):
    return [x for x in iterable1 if func1(x) == True]


# 31.3 reduce v1
def reduce_v1(func1, iterable1):
    result = func1(iterable1.pop(0), iterable1.pop(1))
    for x in iterable1:
        result = func1(x, result)
    return result


# 32. find_palidromes()
def find_palidromes(filename):
    result = []
    with open(filename) as a_file:
        for line in a_file:
            if is_palindrome_advanced(line):
                result.append(line)
    return result


# 33. find_semordnilaps()
def find_semordnilaps(filename):
    result = []
    with open(filename) as a_file:
        words = a_file.read().split()
    for word in words:
        for w in words:
            if word == reverse(w):
                result.append(w)
    return result


# 34. char_freq_table()
def char_freq_table(filename='data/the-dream.md'):
    # text=''
    with open(filename) as a_file:
        text = a_file.read()
    str = 'abcdefghijklmnopqrstuvwxyz'
    for char in str:
        print('{}: {}'.format(char, text.count(char)))


# 35. speak_ICAO()
def speak_ICAO(input_str='Myopia'):
    input_str = input_str.lower()
    result = ''
    d = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot',
         'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
         'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec', 'r': 'romeo',
         's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey',
         'x': 'x-ray', 'y': 'yankee', 'z': 'zulu'}
    for char in input_str:
        result += d[char] + ' '
    return result


# 36. find_hapax_legomenons()
def find_hapax_legomenons(filename):
    result = []
    with open(filename) as a_file:
        txt = a_file.read()
    words = re.findall('\w+', txt)
    words = [word.lower() for word in words]
    for word in words:
        if words.count(word) == 1:
            result.append(word)
    return set(result)


# 37. copy_file_count_lines()
def copy_file_count_lines(filename):
    line_num = 1
    with open('output_37.md', mode='w') as output_file:
        with open(filename) as input_file:
            for line in input_file:
                out = str(line_num) + ' ' + line
                output_file.write(out)
                line_num += 1


# 38. average_word_length()
def average_word_length(filename):
    with open(filename) as a_file:
        words = re.findall(r'\w+', a_file.read())
        total = 0
        num = 0
        for word in words:
            total += len(word)
            num += 1
    avg = total / num
    return int(avg)


# 39.guess_the_number_game()
def guess_the_number_game():
    guess = 0
    num_guesses = 0
    user_name = input('Hello! What is your name?')
    print('Well, {}, I am thinking of a number between 1 and 20.'.format(user_name))
    num = random.randrange(1, 21)
    while guess != num:
        guess = int(input('Take a guess.'))
        if guess < num:
            print('Your guess is too low.')
        else:
            print('Your guess is too high.')
        num_guesses += 1
    print('Good job, {}! You guessed my number in {} guesses!'.format(user_name, num_guesses))


# 40. anagram_game()
def anagram_game(list):
    word = random.sample(list, 1)[0].lower()
    puzzle = random.sample([''.join(p) for p in itertools.permutations(word, len(word))], 1)[0]
    guess = ''
    print('Colour word anagram: {}'.format(puzzle))
    while (word != guess):
        guess = input('Guess the colour word!').lower()
    print('correct!!')


# 41. lingo()
def lingo(word, guess):
    d = []
    result = ''
    length = len(word)
    for i, char in enumerate(guess):
        if char in word:
            if i < length:
                if char == word[i]:
                    result += '[' + char + ']'
                else:
                    result += '(' + char + ')'
            else:
                result += '(' + char + ')'
        else:
            result += char
    return result


# 42. split_sentences()
def split_sentences(filename):
    with open(filename) as a_file:
        input_str = a_file.read().rstrip()
    input_str = re.sub(r'(?<!(Dr)|(Mr))\. (?![a-z])', '.\n', input_str)
    input_str = re.sub(r'([!?]) ', r'\1\n', input_str)
    return input_str


# 43. find_anagrams()
def find_anagrams(filename):
    dict_anag = {}
    has_anag = {}
    result = []
    with open(filename) as a_file:
        for word in a_file:
            word = word.rstrip()
            index = ''.join(sorted(word))
            # print(index)
            if index in dict_anag.keys():
                if has_anag[index]:
                    result.append(word)
                else:
                    has_anag[index] = True
                    result.append(dict_anag[index])
                    result.append(word)
            else:
                dict_anag[index] = word
                has_anag[index] = False
    return result


# 44. validate_brackets()
def validate_brackets(str):
    counter = 0
    if len(str) % 2 != 0:
        return False
    for char in str:
        if char == '[':
            counter += 1
        elif char == ']':
            counter -= 1
        if counter < 0:
            return False
    if counter == 0:
        return True
    else:
        return False


# 44.b generate_brackets()
def generate_brackets(N):
    bracks = ['[', ']']
    result = ''
    for i in range(N):
        result += bracks[random.randint(0, 1)]
    return result
    # print(result)


# 44. Generate matching brackets
def abc():
    bracks = ']'
    while not validate_brackets(bracks):
        bracks = generate_brackets(6)
    print(bracks)


# 45. words_domino() too slow
# Fixed speed issues by using defaultdict. My version gives better output(with more words), that's why test fails
def words_domino(filename):
    chain_longest = []
    dict_domino=defaultdict(list)
    with open(filename) as a_file:
        words = re.findall(r'\w+', a_file.read())
    for word in words:
        dict_domino[word[0]].append(word)
    # print(dict_domino)
    for word in words:
        chain = Chain(word, dict_domino)
        if len(chain) > len(chain_longest):
            chain_longest = chain
    print(chain_longest)
    print(len(chain_longest)==len(set(chain_longest)))
    return chain_longest


def Chain(starting_word, iterable_dict):
    # print(starting_word)
    # print(starting_word[-1])
    # print(iterable_dict)
    iterable_dict[starting_word[0]].remove(starting_word)
    chain = [starting_word]
    max_subchain = []
    it=iterable_dict[starting_word[-1]]
    if it:
        for w in it:
            # iterable_dict[starting_word[-1]].remove(w)
            subchain = Chain(w, iterable_dict)
            # iterable_dict[starting_word[-1]].append(w)
            if len(subchain) > len(max_subchain):
                max_subchain = subchain
        chain.extend(max_subchain)
    iterable_dict[starting_word[0]].append(starting_word)
    return chain
