import random  # To guess some number.
import math #  math lib is good to deal with Mathematics Problems.
x=int(input("x=?")) # X is the number you what to get the sqr root of it.
g= random.randint(1, 100) # g is the number we guessed.
while not math.isclose(x, g*g, abs_tol=0): # while loop to check if geuss is correct and close enough.
    print(g) # optional... to view the current G while runtime.
    g=(g+x/g)/2 # The main formula for finding Sqr Root.
else: # what to say. ... HAHA.
    print(round(g, 8)) # The final value (Square root of any Number.).
