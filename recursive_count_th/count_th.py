'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    nope = 'f' not in word and 'h' not in word
    # Base case 1
    if nope:
        return 0
    # Base case 2
    elif word == '':
        return 0
    # Otherwise, run the recursive part
    else: 
        return word.count('th')

print(count_th('the'))
print(count_th('thesis'))
print(count_th('thethethe'))