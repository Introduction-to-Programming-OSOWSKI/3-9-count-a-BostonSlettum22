def countA(w):
    bazinga = 0

    for i in range(0,len(w)):
        bazinga = bazinga + i
        if bazinga == len("a"):
            return len("a")

print(countA("bazinga"))

