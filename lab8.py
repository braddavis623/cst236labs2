"""lab8.py"""

import inspect
import unittest

classes = inspect.getmembers(unittest, predicate=inspect.isclass)

for c in classes:
    members = inspect.getmembers(c)
    print c
    for m in members:
        print "\t", m
