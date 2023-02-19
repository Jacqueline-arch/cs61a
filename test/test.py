# def num_eights(n):
#     """Returns the number of times 8 appears as a digit of n.

#     >>> num_eights(3)
#     0
#     >>> num_eights(8)
#     1
#     >>> num_eights(88888888)
#     8
#     >>> num_eights(2638)
#     1
#     >>> num_eights(86380)
#     2
#     >>> num_eights(12345)
#     0
#     >>> num_eights(8782089)
#     3
#     """
#     if n == 0:
#         return 0
#     if n % 10 == 8:
#         return 1 + num_eights( n // 10 )
#     else:
#         return 0 + num_eights( n // 10)
    
# def pingpong(n):
#     """Return the nth element of the ping-pong sequence.

#     >>> pingpong(8)
#     8
#     >>> pingpong(10)
#     6
#     >>> pingpong(15)
#     1
#     >>> pingpong(21)
#     -1
#     >>> pingpong(22)
#     -2
#     >>> pingpong(30)
#     -2
#     >>> pingpong(68)
#     0
#     >>> pingpong(69)
#     -1
#     >>> pingpong(80)
#     0
#     >>> pingpong(81)
#     1
#     >>> pingpong(82)
#     0
#     >>> pingpong(100)
#     -6
#     """
#     def helper(i, value, dir):
#         if i == n:
#             return value
#         if (i + 1) % 8 == 0 or num_eights(i + 1) > 0:
#             return helper(i+1, value + dir, -dir)  
#         else:
#             return helper(i+1, value + dir, dir)
#     return helper(1, 1, 1)

#     # i = 2
#     # value = 1
#     # dir = 0
#     # while i <= n:
#     #     if int(dir % 2) == 0:
#     #         value += 1
#     #     else: 
#     #         value -= 1
#     #     if i % 8 == 0 or num_eights(i) > 0:
#     #         dir += 1
#     #     i += 1
#     # return value
# def next_larger_coin(coin):
#     """Returns the next larger coin in order.
#     >>> next_larger_coin(1)
#     5
#     >>> next_larger_coin(5)
#     10
#     >>> next_larger_coin(10)
#     25
#     >>> next_larger_coin(2) # Other values return None
#     """
#     if coin == 1:
#         return 5
#     elif coin == 5:
#         return 10
#     elif coin == 10:
#         return 25


# def next_smaller_coin(coin):
#     """Returns the next smaller coin in order.
#     >>> next_smaller_coin(25)
#     10
#     >>> next_smaller_coin(10)
#     5
#     >>> next_smaller_coin(5)
#     1
#     >>> next_smaller_coin(2) # Other values return None
#     """
#     if coin == 25:
#         return 10
#     elif coin == 10:
#         return 5
#     elif coin == 5:
#         return 1
    
def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)    # The top left (the point of the triangle)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    if column > row:
        return 0
    if row == 0 and column == 0:
        return 1
    if column < 0 or row < 0:
        return 0 
    else:
        return pascal(row - 1, column) + pascal (row - 1, column - 1) 