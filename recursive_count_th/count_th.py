'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    """ Returns the count of `th` occurrences in a word """
    return word.count(" ") if "th" not in word else count_th(word.replace("th",
                                                                          " ", 1))
