# verifica se os três lados podem formar um triângulo
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a < b + c and b < a + c and c < a + b:
    print("Forma um triângulo.")
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("Área do triângulo é:", area)
else:
    print("Não forma triângulo. Valores:", a, b, c)
