'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
# 
recursion needs a base case.
if the word is only one letter then there are no "th"s and should return 0
else we need a count to keep track of the number of "th"s
this could be called count
we need to check the string to see "t" and "h" are next to each other
we can check that by splicing and starting at the beginning of the string
if the spliced string matches "th" then we increase our count by 1
call the function again but this time moving the beginning of the string over by one we can also do thi by splicing
'''

def count_th(word):
    # TBC
    #* Base case
    if len(word) < 1:
        return 0
    else:
        #* initialize a variable to keep track of th
        count = 0
        #* splice the word two letters at a time to check if it matches th
        if word[0:2] == "th":
            #* if it does increase the count 
            count += 1
        #* return the count and call the function again but splice offthe first index since we already checked if it and its neighbor to the right are th
        return count+count_th(word[1:])
print(count_th("lajsdfhtthldkjsflthljdsth"))