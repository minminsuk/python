def factorial_iterative(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

factorials_iterative = [factorial_iterative(i) for i in range(3, 8)]
for i, value in enumerate(factorials_iterative, start=3):
        print(f"{i}! = {value}")