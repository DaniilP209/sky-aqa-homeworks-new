def fizz_buzz(n):
    # Перебираем числа от 1 до n
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:  # Число делится на 3 и на 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Число делится только на 3
            print("Fizz")
        elif i % 5 == 0:  # Число делится только на 5
            print("Buzz")
        else:  # Во всех остальных случаях
            print(i)

# Вызываем функцию с числом 17
fizz_buzz(17)