import sqlite3
from datetime import datetime

con = sqlite3.connect("imc.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    peso REAL,
    altura REAL,
    imc REAL,
    classificacao TEXT,
    data_calculo TEXT
)
""")
con.commit()


def calcular_imc(peso, altura):
    altura_m = altura / 100
    imc = peso / (altura_m ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade I"
    elif imc < 39.9:
        return "Obesidade II"
    else:
        return "Obesidade III"

def salvar_no_banco(nome, idade, peso, altura, imc, classificacao):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    cur.execute("""
        INSERT INTO pacientes (nome, idade, peso, altura, imc, classificacao, data_calculo)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (nome, idade, peso, altura, imc, classificacao, data))
    con.commit()

def listar_registros():
    cur.execute("SELECT * FROM pacientes")
    registros = cur.fetchall()
    print("\n--- Histórico de IMC ---")
    for r in registros:
        print(f"ID: {r[0]} | Nome: {r[1]} | IMC: {r[5]:.2f} | Classificação: {r[6]} | Data: {r[7]}")


while True:
    print("\n CALCULADORA DE IMC ")
    print("1 - Calcular IMC")
    print("2 - Ver histórico")
    print("3 - Sair")

    opc = input("Escolha: ")

    if opc == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (cm): "))

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        print(f"\nIMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")

        salvar_no_banco(nome, idade, peso, altura, imc, classificacao)
        print("Salvo no banco com sucesso!")

    elif opc == "2":
        listar_registros()

    elif opc == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

