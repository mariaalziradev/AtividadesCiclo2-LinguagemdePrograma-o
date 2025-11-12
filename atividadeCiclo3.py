from tkinter import *

def calcular_imc():
    try:
        peso = float(caixa_peso.get())
        altura = float(caixa_altura.get()) / 100
        imc = peso / (altura * altura)

        if imc < 18.5:
            resultado["text"] = f"IMC: {imc:.2f} (Abaixo do peso)"
        elif imc < 24.9:
            resultado["text"] = f"IMC: {imc:.2f} (Peso normal)"
        elif imc < 29.9:
            resultado["text"] = f"IMC: {imc:.2f} (Sobrepeso)"
        elif imc < 34.9:
            resultado["text"] = f"IMC: {imc:.2f} (Obesidade I)"
        elif imc < 39.9:
            resultado["text"] = f"IMC: {imc:.2f} (Obesidade II)"
        else:
            resultado["text"] = f"IMC: {imc:.2f} (Obesidade III)"
    except:
        resultado["text"] = "Erro! Digite números válidos."

def reiniciar():
    caixa_idade.delete(0, END)
    caixa_peso.delete(0, END)
    caixa_altura.delete(0, END)
    caixa_endereco.delete(0, END)
    resultado["text"] = ""

janela = Tk()
janela.title("Calculo de IMC")

texto_orientacao = Label(janela, text="Digite sua idade")
texto_orientacao.grid(column=0, row=0)
caixa_idade = Entry(janela)
caixa_idade.grid(column=1, row=0)

texto_orientacao = Label(janela, text="Digite seu peso (em kg)")
texto_orientacao.grid(column=0, row=1)
caixa_peso = Entry(janela)
caixa_peso.grid(column=1, row=1)

texto_orientacao = Label(janela, text="Digite sua altura (em cm)")
texto_orientacao.grid(column=0, row=2)
caixa_altura = Entry(janela)
caixa_altura.grid(column=1, row=2)

texto_orientacao = Label(janela, text="Digite seu endereço")
texto_orientacao.grid(column=0, row=3)
caixa_endereco = Entry(janela)
caixa_endereco.grid(column=1, row=3)

botao = Button(janela, text="Calcular", command=calcular_imc)
botao.grid(column=0, row=4)

botao_reiniciar = Button(janela, text="Reiniciar", command=reiniciar)
botao_reiniciar.grid(column=1, row=4)

resultado = Label(janela, text="")
resultado.grid(column=0, row=5, columnspan=2)

janela.mainloop()
