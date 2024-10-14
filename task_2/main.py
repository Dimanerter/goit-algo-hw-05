from typing import Callable
import re


def generator_numbers(text: str):
    # Регулярное выражение для поиска чисел, разделённых пробелами
    pattern = r"\s\d+\.?\d+\s"
    # Итерируем по всем совпадениям, найденным регулярным выражением
    for num in re.findall(pattern, text):
        # Преобразуем каждое найденное число в float и возвращаем через yield
        yield float(num)


def sum_profit(text: str, func: Callable):
    # Вызываем генератор и суммируем все его значения
    return sum(func(text))


def main():
    text = """Загальний дохід працівника складається
    з декількох частин: 1000.01
    як основний дохід, доповнений
    додатковими надходженнями 27.45 і 324.00 доларів."""
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__ == "__main__":
    main()
