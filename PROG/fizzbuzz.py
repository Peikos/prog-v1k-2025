# Print getallen 1 t/m 100
# Als getal deelbaar door 3: print Fizz
# Als getal deelbaar door 5: print Buzz
# Als beide: print FizzBuzz

getal = 100

for i in range(1, getal + 1):
    if i % 3 == 0 and i % 5 == 0: # if i % 15 == 0
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)