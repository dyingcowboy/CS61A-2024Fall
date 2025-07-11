
class Link:
    empty=()
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first=first
        self.rest=rest
    def __repr__(self):
        if self.rest:
            rest_repr=', '+repr(self.rest)
        else:
            rest_repr=''
        return f'Link({repr(self.first)}{rest_repr})'
s=Link(3, Link(4, Link(5)))
print(s)

square, odd = lambda x: x*x, lambda x: x % 2 ==1

def range_link(start, end):
    """Return a Link containing consecutive integers from start to end.
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))"""
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start+1, end))

def map_link(f, s):
    """Return a Link that contains f(x) for each x in Link s.
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))"""
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """Return a Link that contains only the elements x of Link s for which f(x) is a True value
    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))"""

    if s is Link.empty:
        return s
    filter_rest = filter_link(f, s.rest)
    if f(s.first):
        return Link(s.first, filter_rest)
    else:
        return filter_rest

def add(s, v):
    """Add v to an ordered list s with no repeats, returning modifying s."""
    # if s.first == v:
    #     return s
    # if v<=s.first:
    #     temp = s.first
    #     s.first = v
    #     s.rest = Link(temp, s.rest)
    #     return s
    # if s.rest == Link.empty:
    #     s.rest = Link(v, Link.empty)
    #     return s
    # return Link(s.first, add(s.rest, v))
    assert s is not Link.empty
    if s.first > v :
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s
print(add(map_link(square, range_link(3, 6)), 8))