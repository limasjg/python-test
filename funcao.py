def minha_funcao(valor1, valor2):
    return valor1 + valor2

contador = 1

while contador <= 3:
    valor1 = int(input("Valor1: "))
    valor2 = int(input("Valor2: "))

    resposta = minha_funcao(valor1, valor2)
    print(valor1, "+", valor2, "=", resposta)

    contador += 1