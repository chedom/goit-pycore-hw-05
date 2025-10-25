from typing import Iterable, Callable
import re


real_number_pattern = r'[-+]?\d+(?:\.\d+)?'

def generator_numbers(text: str) -> Iterable:
    for word in text.split(" "):
        if re.fullmatch(real_number_pattern, word.strip()):
            yield float(word.strip())


def sum_profit(text: str, func: Callable[[str], Iterable]) ->float:
    profit = 0

    for  num in func(text):
        profit += num

    return profit


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
