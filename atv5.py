# inverte as frases
frase = input("Digite uma frase: ")

palavras = frase.split()
nova_frase = ""

for p in palavras:
    invertida = ""
    for letra in p:
        invertida = letra + invertida
    nova_frase = nova_frase + invertida + " "

print("Frase invertida:", nova_frase)
