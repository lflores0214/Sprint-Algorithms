#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n)
the fn runs until it hits a < n^3
    a increases at a rate of n^2
    dividing n^3 by n^2 gets you n^1 -> BigO == O(n)


b)
O(nlogn)
fn runs until it reaches the end of n
assignment takes a constant time 1
runs while is less than n
j increases at rate of 2j
sum increases at rate of 1
since j is increasing independent of n we need to take that into account
j gets doubled each time so the time it takes to reach n is log n

(n * 1)(logn) -> n*logn = O(nlogn)

c)
O(n)
The more bunnies you add the more time it takes to run the function based the amount amount of bunnies if bunnies = 1 it only runs the function twice

## Exercise II
if f starts at n / 2 (f= n//2) and the egg breaks you can cut the f by half again and check if the egg breaks at that floor if it does you cut f in half and try again (f = f/2) if the egg doesn't break than you cut f in half again (f = f/2) but this time you go up

this is basically the same logic binary search where you shorten your search field by half each time until you find your target Big O will be O(logn)

