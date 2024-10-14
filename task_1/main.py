def caching_fibonacci():
    # Инициализируем словарь для хранения значений Фибоначчи
    cash = {}
    
    # создаем вложенную функцию для вычисления числа Фибоначчи
    def fibonacci(n) -> int:
        # Если n меньше или равно 0, возвращаем 0
        if n <= 0:
            return 0
        
        # Если n равно 1, возвращаем 1
        if n == 1:
            return 1
        
        # Если значение для n уже есть в кэше, возвращаем его
        if n in cash:
            return cash[n]
        
        # вычисление значения для n через рекурсию
        cash[n] = fibonacci(n-1) + fibonacci(n-2)
        return cash[n]

    # Возвращаем функцию fibonacci для последующего использования
    return fibonacci

def main():
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()

    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610

if __name__ == "__main__":
    main()