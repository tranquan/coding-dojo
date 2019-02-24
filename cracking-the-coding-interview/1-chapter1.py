import os
import array
import copy

#1. check if a string has unique characters
# -> count chars in string, if a char occur more than two times, then it is not unique
# * should ask whether ASCII or Unicode. Case-sensitive or not
def is_unique(input):
    # standard ascii has 128 chars (extended has 256 chars)
    if len(input) > 128: return False
    # count apperance
    chars_counts = [0] * 128
    input = input.lower()
    for char in input:
        index = ord(char)-ord('a')
        if chars_counts[index] > 0:
            return False
        chars_counts[index] = 1
    return True

# t = is_unique("this is not unique")
# print(t)

#2. given two string, check whether one is permutation of the other
# -> count all chars of each string and compare. 
# -> if a string permutaion of the other, it should have same chars counts
def is_permutation(str1, str2):
    if len(str1) != len(str2): return False
    
    chars_counts1 = dict()
    chars_counts2 = dict()
    
    for char in str1:    
        if char in chars_counts1:
            chars_counts1[char] += 1
        else:
            chars_counts1[char] = 1
    
    for char in str2:
        if char in chars_counts2:
            chars_counts2[char] += 1
        else:
            chars_counts2[char] = 1

    for key in chars_counts1.keys():
        if key not in chars_counts2:
            return False
        if chars_counts1[key] != chars_counts2[key]:
            return False

    return True

# t = is_permutation("hello", "ollhe")
# print(t)

#3. replace all space in a string with '%20'
#-> trim then replace
def urlencode(str, n):
    chars = list(str)
    
    # trim
    for i in range(0, len(chars)):
        if chars[i] == ' ': chars[i] = ''
        else: break
    for i in range(len(chars)-1, -1, -1):
        if chars[i] == ' ': chars[i] = ''
        else: break
    
    # replace
    new_str = "".join(chars)
    new_chars = list(new_str)
    print(new_chars)
    for i in range(0, len(new_chars)):
        if new_chars[i] == ' ':
            new_chars[i] = '%20'
    
    return "".join(new_chars)

# t = urlencode("Mr John Smith    ", 13)
# print(t)

#4. check permutation has palindome
#-> count all chars, if has more then 2 char count odd -> False
def is_permutation_palindrome(str):
    if len(str) == 0: return False
    
    str = str.lower()
    chars_counts = dict()
    
    for char in str:
        if char != ' ':
            if char in chars_counts:
                chars_counts[char] += 1
            else:
                chars_counts[char] = 1
    
    total_odds = 0

    for key in chars_counts.keys():
        # count odds
        if chars_counts[key] % 2 == 1:
            total_odds += 1
        # the check should be at bottom
        # the last increase key will break in for loop if the check is put on top 
        if total_odds > 1:
            return False

    return True

# t = is_permutation_palindrome("Tact Coa")
# print(t)

#5. check if a string is one edit
def is_one_edit(org_str, mod_str):
    len_org = len(org_str)
    len_mod = len(mod_str)
    
    if abs(len_org - len_mod) > 1:
        return False
    
    if len_org == len_mod:
        return is_one_edit_by_replace(org_str, mod_str)
    elif len_org > len_mod:
        return is_one_edit_by_remove(org_str, mod_str)
    else:
        return is_one_edit_by_remove(mod_str, org_str)

def is_one_edit_by_replace(org_str, mod_str):
    diff = 0
    for i in range(0, len(org_str)):
        if org_str[i] != mod_str[i]:
            diff += 1
        if diff >= 2:
            return False
    return True


def is_one_edit_by_remove(org_str, mod_str):
    diff = 0
    s = 0
    l = 0
    while s < len(mod_str):
        if org_str[l] != mod_str[s]:
            diff += 1
            l += 1
        else:
            s += 1
            l += 1
        if l >= len(org_str):
            diff = 2
            break
    if diff > 1: return False
    else: return True

# t = is_one_edit("hello", "helo")
# print(t)

#6. string compression
def compress(strng):
    
    if len(strng) == 0:
        return strng

    should_compress = False
    chars = list(strng)
    queue = list()
    
    current_char = chars[0]
    current_count = 1
    for i in range(1, len(chars)):
        if chars[i] != current_char:
            queue.append((current_char, current_count))
            if current_count >= 3:
                should_compress = True
            current_char = chars[i]
            current_count = 1
        else:
            current_count += 1
            if i == len(chars)-1:
                queue.append((current_char, current_count))
    
    if should_compress:
        new_str = ""
        while len(queue) > 0:
            char = queue.pop(0)
            new_str += char[0] + str(char[1])
        return new_str
    else:
        return strng

# t = compress("")
# print(t)

#7. rotate matrix
# -> rotate each 1/4 of image
def rotate_image(image1, n):
    image = copy.deepcopy(image1)
    
    m = n/2
    if n % 2 == 1: m += 1

    for y in range(0, n/2):
        for x in range(0, m):

            x1 = (n-1)-y
            y1 = x 
            
            x2 = (n-1)-y1
            y2 = x1
            
            x3 = (n-1)-y2
            y3 = x2 

            temp = image[y][x]
            image[y][x] = image[y1][x1]
            image[y1][x1] = image[y2][x2]
            image[y2][x2] = image[y3][x3]
            image[y3][x3] = temp

    return image

#7. dum array
def print_array(arr, n):
    for i in range(0, n):
        row = map(lambda x: "%2d" % x, arr[i])
        print(row)

# 7. test 1
# t0 = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [13, 14, 15, 16],
#     [17, 18, 19, 20]
# ]
# print_array(t0, 4)
# print("rotate:")
# t = rotate_image(t0, 4)
# print_array(t, 4)

# 7. test 2
# t1 = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
# print_array(t1, 5)
# print("rotate:")
# t = rotate_image(t1, 5)
# print_array(t, 5)

#8. set row & colum to zero if cell is zero
# -> go through arr, put all zero cell column & row into queue and set later
def set_zero(arr, m, n):
    columns = list()
    rows = list()
    
    for y in range(0, n):
        for x in range(0, m):
            if arr[y][x] == 0:
                columns.append(y)
                rows.append(x)
    
    while len(columns) > 0:
        y = columns.pop(0)
        for x in range(0, m):
            arr[y][x] = 0

    while len(rows) > 0:
        x = rows.pop(0)
        for y in range(0, n):
            arr[y][x] = 0
    
    return arr

# t0 = [
#     [1, 2, 3, 4],
#     [5, 0, 7, 8],
#     [13, 14, 15, 16],
#     [17, 18, 0, 20]
# ]
# t = set_zero(t0, 4, 4)
# print(t)

#9. check string rotation
def is_rotation(org_strng, mod_strng):
    if len(org_strng) != len(mod_strng): return False
    
    org_strng = org_strng.lower()
    mod_strng = mod_strng.lower()
    
    dup_mod_strng = mod_strng + mod_strng
    if org_strng in dup_mod_strng:
        return True
    else:
        return False

# t = is_rotation("watwat", "twatwa")
# print(t)