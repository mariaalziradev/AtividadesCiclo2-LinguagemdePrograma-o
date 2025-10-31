# Programa que transforma idade em dias para anos, meses e dias
dias = int(input("Digite sua idade em dias: "))

anos = dias // 365
meses = (dias % 365) // 30
dias = (dias % 365) % 30

print("Você tem", anos, "anos,", meses, "meses e", dias, "dias.")
