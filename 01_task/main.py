from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    cache = dict[int, int]() # create cache for optimizing calculation

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache: # check cache before computation
            return cache.get(n)
        # store calculated value to be accessed for next calls
        cache[n] = fibonacci(n-1) + fibonacci(n-2)

        return cache.get(n)

    return fibonacci

fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610