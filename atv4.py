# verifica os números primos de 1 até 100
for num in range(1, 101):
    if num > 1:
        primo = True
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break
        if primo:
            print(num, "é primo")
