# def make_even(t):
#     """
#     >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
#     >>> make_even(t)
#     >>> t.label
#     2
#     >>> t.branches[0].branches[0].label
#     4
#     """
#     def f(x):
#         if x % 2 == 0:
#             return x 
#         else: 
#             return x + 1
#     t.label = f(t.label)
#     for i in t.branches:
#         if i.is_leaf():
#             i.label = f(i.label)
#         else:
#             make_even(i)

# def cumulative_mul(t):
#     """Mutates t so that each node's label becomes the product of all labels in
#     the corresponding subtree rooted at t.

#     >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
#     >>> cumulative_mul(t)
#     >>> t
#     Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
#     >>> otherTree = Tree(2, [Tree(1, [Tree(3), Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
#     >>> cumulative_mul(otherTree)
#     >>> otherTree
#     Tree(5040, [Tree(60, [Tree(3), Tree(4), Tree(5)]), Tree(42, [Tree(7)])])
#     """
    
#     for i in t.branches:
#         if i.is_leaf():
#             i.label = i.label
#         else:
#             i = cumulative_mul(i)
#     product = t.label
#     for i in t.branches:
#         product *= i.label
#     t.label = product
    



# def prune_small(t, n):
#     """Prune the tree mutatively, keeping only the n branches
#     of each node with the smallest labels.

#     >>> t1 = Tree(6)
#     >>> prune_small(t1, 2)
#     >>> t1
#     Tree(6)
#     >>> t2 = Tree(6, [Tree(3), Tree(4)])
#     >>> prune_small(t2, 1)
#     >>> t2
#     Tree(6, [Tree(3)])
#     >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
#     >>> prune_small(t3, 2)
#     >>> t3
#     Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
#     """
#     while len(t.branches) > n:
#         largest = max(t.branches, key=lambda x: x.label)
#         t.branches.remove(largest)
#     for i in t.branches:
#         prune_small(i, n)


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    # def bst_min(t):
    #     if t.is_leaf():
    #         return t.label
    #     else:
    #         return min(t.label, bst_min(t.branches[0]))
        
    # def bst_max(t):
    #     if t.is_leaf():
    #         return t.label
    #     else:
    #         return max(t.label, bst_max(t.branches[-1]))
   
   
    # if t.is_leaf():
    #     return True
    # elif len(t.branches) == 1:
    #     if bst_min(t) <= t.label <= bst_max(t):
    #         return True 
    # elif len(t.branches) == 2:
    #     return bst_max(t.branches[0]) <= t.label <= bst_min(t.branches[1]) and is_bst(t.branches[0]) and is_bst(t.branches[1])
    # else:
    #     return False
    def helper(t:'Tree', min_val:int, max_val:int) -> bool:
        if t.label > max_val or t.label <= min_val: return False
        n = len(t.branches)
        if n > 2 : return False
        if n == 0: return True
        if n == 1: return helper(t.branches[0], min_val, t.label) if t.label >= t.branches[0].label else helper(t.branches[0], t.label, max_val)
        return helper(t.branches[0], min_val, t.label) and helper(t.branches[1], t.label, max_val)
    return helper(t,-2**31,2**31-1)

def add_trees(t1, t2):
    """
    >>> numbers = Tree(1,
    ...                [Tree(2,
    ...                      [Tree(3),
    ...                       Tree(4)]),
    ...                 Tree(5,
    ...                      [Tree(6,
    ...                            [Tree(7)]),
    ...                       Tree(8)])])
    >>> print(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print(add_trees(Tree(2), Tree(3, [Tree(4), Tree(5)])))
    5
      4
      5
    >>> print(add_trees(Tree(2, [Tree(3)]), Tree(2, [Tree(3), Tree(4)])))
    4
      6
      4
    >>> print(add_trees(Tree(2, [Tree(3, [Tree(4), Tree(5)])]), \
    Tree(2, [Tree(3, [Tree(4)]), Tree(5)])))
    4
      6
        8
        5
      5
    """
    if not t1:
        return t2
    if not t2:
        return t1
    
    new_label = t1.label + t2.label
    t1_branches, t2_branches = t1.branches, t2.branches
    length_t1, length_t2 = len(t1.branches), len(t2.branches)
    if length_t1 < length_t2:
        t1_branches += [ None for a in range(length_t1, length_t2)]
    # [ a + b for a, b in zip(t1.branches, t2.branches)]

    elif length_t2 < length_t1:
        t2_branches += [ None for a in range(length_t2, length_t1)]
    return Tree(new_label, [add_trees(a, b) for a, b in zip(t1.branches, t2.branches)])
 

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
    