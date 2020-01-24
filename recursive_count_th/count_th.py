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
    # Otherwise, run the count of th
    else: 
        return word.count('th')

print(count_th('the'))
print(count_th('thesis'))
print(count_th('thethethe'))

# Not sure above function counts as "recursion" (although it's a lot better imo) so here's a less efficient one.

def less_efficient_count_th(word):
    if len(word) <= 0:
        return 0
    if word[0] + word[1] == 'th':
        print('Recursive tally: 1')
        return 1
    less_efficient_count_th(word[2:])
    print('Recursive tally: 1') # Confirmed working because should only it on
    return 1

# This isn't perfect but calling it done as I'd use the first take in real life.

print(less_efficient_count_th('the'))
print(less_efficient_count_th('thesis'))
print(less_efficient_count_th('thethethe'))