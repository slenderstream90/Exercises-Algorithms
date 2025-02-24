import random

#counts the number of "B" (black hats) in a list
def blackCounter(lst):
    c = 0
    for i in lst:
        if i == "B":
            c += 1
    return c

#generate a list of prisions with randomly assigned hat colors ("B" or "W")
p = [random.choice("B""W") for i in range(int(input("num. of prisioners ")))]

'''p = ["B","B","B","B","W"]''' #test list

print(p) #print the assigned hats

g = [] #list of guesses

#last prisioner (first counting from the left) sees how all hats in front and responds according to parity
if blackCounter(p[1:])%2 != 0:
    g.append("B")
else: 
    g.append("W")

#all the other prisioners make a guess based on the parity of previous responses and the hats they see
for i in range(len(p[1:])):
    if blackCounter(g) % 2 == 0: #if the black hats' guesses made so far are even
        if blackCounter(p[i+2:])%2 != 0: #if the black hats the prisioner see is odd
            g.append("B")
        else:
            g.append("W")
    elif blackCounter(g) % 2 != 0: #if the black hats' guesses made so far are odd
        if blackCounter(p[i+2:])%2 == 0: #if the black hats the prisioner see is even
            g.append("B")
        else:
            g.append("W")

print(g) #print the prisioners' guesses

#count the number of correct guesses
x = 0
for i in range(len(g)):
    if g[i] == p[i]:
        x += 1

print(f"{x} out of {len(p)} prisioners were saved") # print the number of prisioners saved

#determines the success of the algorithm
if (len(p)-x) > 1:
    print("failed")
else:
    print("success"
