#!/usr/bin/env python
#
# Luke Southam <luke@devthe.com>
# GCJ Problem C. Fair and Square
#

from math import sqrt, ceil
from multiprocessing import Pool

square = lambda n: n**2
squares = lambda min_, max_: map(square, range(int(ceil(sqrt(min_))), int(sqrt(max_)) + 1))
is_palindrome = lambda n: str(n) == str(n)[::-1]
solve = lambda min_, max_: len(filter(is_palindrome, squares(min_, max_)))

T = int(raw_input())

inputs = []

pool = Pool(processes=4)

for test in xrange(T):
	print "Case #%i: %s" % (test + 1, '\n'.join(map(str, squares(*map(int, raw_input().split())))))

# P.S
# Very easy solution in python, but not for large inputs.
