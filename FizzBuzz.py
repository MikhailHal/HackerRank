def fizzBuzz(n):
    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 != 0 and i%5 != 0:
            print(i)
        elif i%3 != 0:
            print("Buzz")
        else:
            print("Fizz")

fizzBuzz(15)