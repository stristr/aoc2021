# 911/207
# 7:28/24:34
from sys import stdin
from itertools import permutations

def parse(line):
    [a, b] = line.split(' | ')
    return tuple(a.split(' ')), tuple(b.split(' '))

data = list(map(parse, stdin.read().strip().split('\n')))
dict = {
    'abcefg':  '0',
    'cf':      '1',
    'acdeg':   '2',
    'acdfg':   '3',
    'bcdf':    '4',
    'abdfg':   '5',
    'abdefg':  '6',
    'acf':     '7',
    'abcdefg': '8',
    'abcdfg':  '9',
}

translate = lambda chars, lexicon: ''.join(sorted(lexicon[c] for c in chars))
resolve = lambda out, lexicon: int(''.join(dict[translate(chars, lexicon)] for chars in out))
all_lexicons = list(map(lambda permutation: {k: v for k, v in zip(permutation, 'abcdefg')}, permutations('abcdefg')))
lexicons = {
    out: next(lexicon for lexicon in all_lexicons
    if all(translate(chars, lexicon) in dict for chars in nums)) for nums, out in data}

print('a', sum(1 for _, out in data for n in out if len(n) in [2, 3, 4, 7]))
print('b', sum(resolve(out, lexicon) for out, lexicon in lexicons.items()))
