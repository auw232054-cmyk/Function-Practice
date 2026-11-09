#Exercise 8. Write and test a recursive function that calculates the sum 1 + 2 + · · · + n for a positive integer n.
def adding_N_integer(n):
      if n<1:
            return 0
      return n+adding_N_integer(n-1)
print(adding_N_integer(4))