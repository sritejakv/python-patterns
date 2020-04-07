"""
:testcase_name lazy_evaluation
:source https://github.com/faif/python-patterns/blob/master/patterns/creational/lazy_evaluation.py
:description Lazily-evaluated property pattern in Python.
Delays the eval of an expr until its value is needed and avoids repeated evals.
"""

import functools


class lazy_property:
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


def lazy_property2(fn):
    attr = '_lazy__' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)

    return _lazy_property


class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        relatives = "Many relatives."
        return relatives

    @lazy_property2
    def parents(self):
        self.call_count2 += 1
        return "Father and mother"


def main():
    """
    >>> Jhon = Person('Jhon', 'Coder')

    >>> Jhon.name
    'Jhon'
    >>> Jhon.occupation
    'Coder'

    # Before we access `relatives`
    >>> sorted(Jhon.__dict__.items())
    [('call_count2', 0), ('name', 'Jhon'), ('occupation', 'Coder')]

    >>> Jhon.relatives
    'Many relatives.'

    # After we've accessed `relatives`
    >>> sorted(Jhon.__dict__.items())
    [('call_count2', 0), ..., ('relatives', 'Many relatives.')]

    >>> Jhon.parents
    'Father and mother'

    >>> sorted(Jhon.__dict__.items())
    [('_lazy__parents', 'Father and mother'), ('call_count2', 1), ..., ('relatives', 'Many relatives.')]

    >>> Jhon.parents
    'Father and mother'

    >>> Jhon.call_count2
    1
    """


if __name__ == "__main__":
    Jhon = Person('Jhon', 'Coder')

    print(Jhon.name)
    print(Jhon.occupation)

    # Before we access `relatives`
    sorted(Jhon.__dict__.items())

    print(Jhon.relatives)

    sorted(Jhon.__dict__.items())

    print(Jhon.parents)

    sorted(Jhon.__dict__.items())

    print(Jhon.parents)
    print(Jhon.call_count2)
