from re import match
from itertools import product

def board(mines):
    w = len(mines[0])
    h = len(mines)
    if board_error(mines, h, w):
        raise ValueError('Invalid board or character.')
    convert_to_list(mines, h, w)
    nums = calc_neighborhoods(mines, h, w)
    return convert_to_string(mines, nums, h, w)

def board_error(m, h, w):
    for i in [0,h-1]:
        if not match("\+\-{%d}\+" % (w - 2), m[i]):
            return True
    for i in range(1, h-1):
        if not match("\|[ *]{%d}\|" %(w - 2), m[i]):
            return True
    return False

def convert_to_list(mines, h, w):
     for i in range(h):
        mines[i] = list(mines[i])
        if len(mines[i]) != w:
            raise ValueError('Board not rectangular.')
            
def calc_neighborhoods(mines, h, w):
    nums = []
    for i in range(h):
        nums.append([0]*w)
    for i, j in product(range(1, h-1), range(1, w-1)):
        if mines[i][j] == '*':
            for k, l in product(range(i-1, i+2), range(j-1, j+2)):
                nums[k][l] += 1
    return nums
    
def convert_to_string(mines, nums, h, w):
    for i,j in product(range(1, h-1), range(1, w-1)):
         if mines[i][j] == ' ' and nums[i][j] > 0:
            mines[i][j] = str(nums[i][j])
    for i in range(h):
        mines[i] = ''.join(mines[i])
    return mines
