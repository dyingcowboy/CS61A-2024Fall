class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)
    
    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines
    
    def __str__(self):
        return '\n'.join(self.indented())
    
    def is_leaf(self):
        return not self.branches
    
def fib_tree(n):
    if n ==0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_label = left.label + right.label
        return Tree(fib_label, [left, right])


def leaves(t):
    """Return a list of leaf labels in Tree T."""
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves

def height(t):
    """Return the number of transitions in the longest path in T"""
    if t.is_leaf():
        return 0
    else:
        return 1+max(height(b) for b in t.branches)
print(height(fib_tree(6)))

def prune(t, n):
    """Prune all sub-trees whose label is n"""
    t.branches = [b for b in t.branches if not b.label==n]
    for b in t.branches:
        prune(b, n)

# Implemnting the Tree Abstration

def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label]+list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n<=1:
        return tree(n)
    else:
        left,right=fib_tree(n-2),fib_tree(n-1)
        return tree(label(left)+label(right),[left,right])

print(fib_tree(5))

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        return sum(count_leaves(b) for b in branches(tree))
print(count_leaves(fib_tree(4)))

def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)],[])
    
print(leaves(fib_tree(4)))

def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t)+1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t),bs)
    
def print_tree(t,indent=0):
    print(' '*indent+str(label(t)))
    for b in branches(t):
        print_tree(b,indent+1)

print_tree(fib_tree(4))

def fact(n):
    if n==0:
        return 1
    
def fact_times(n,k):
    "Return k*n*(n-1)*(n-2)...*!"
    if n==0:
        return k
    else:
        return fact_times(n-1,k*n)
    
numbers=tree(3,[tree(4),tree(5,[tree(6)])])

haste=tree('h',[tree('a',[tree('s'),tree('t')]),tree('e')])

def print_sum(t,so_far):
    so_far+=label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sum(b,so_far)

def count_paths(t,total):
    """Return the number of the path from the root to any node in tree t 
    for which the labels along the path sum to total
    >>> t=tree(3,[tree(-1),tree(1,[tree(2),tree(3)]),tree(1,[tree(-1)])])
    >>> count_paths(t,3)
    2
    >>> count_paths(t,4)
    2
    """
    if total==label(t):
        found=1
    
    else:
        found=0 
    return found+sum([count_paths(b,total-label(t)) for b in branches(t)])




