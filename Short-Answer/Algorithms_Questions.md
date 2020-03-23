# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n): --> runs until it reaches n^3
      a = a + n * n  --> a increases at a rate of a + n^2

      n^3 divided by n^2 would be n^1 so BigO is O(n)
```


```
b)  sum = 0
    for i in range(n): -> fn runs until it reaches the end of  n
      j = 1 -> assignment takes a constant time 1 
      while j < n: -> runs while is less than n
        j *= 2 -> j increases at rate of 2j
        sum += 1 -> sum increases at rate of 1 

        fn 
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0: -> check only happens once constant time 
        return 0 -> return happens once constant time

      return 2 + bunnyEars(bunnies-1) return happens 2 + n-1 times n
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
 if f starts at n / 2 (f= n//2) and the egg breaks you can cut the f by half again and check if the egg breaks at that floor if it does you cut f in half and try again (f = f/2) if the egg doesn't break than you cut f in half again (f = f/2) but this time you go up 
 this is basically the same as binary search where you shorten your search field by half each time until you find your target