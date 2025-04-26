def generates_fibonacchi_sequence(value: int) -> int:
    if value == 1:
        return 1
    elif value == 0:
        return 0
    else:
        return generates_fibonacchi_sequence(value-1) + generates_fibonacchi_sequence(value-2)

n = int(input())
print(generates_fibonacchi_sequence(n))